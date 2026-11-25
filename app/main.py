
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models import Idea, IdeaRequest
from app.store import IdeaStore


def create_app(db_path=None) -> FastAPI:
    app = FastAPI(title="Campus Idea Board")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    store = IdeaStore(db_path)

    @app.exception_handler(RequestValidationError)
    async def invalid_request(request: Request, error: RequestValidationError):
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid request"}
        )

    @app.get("/api/hello")
    def hello():
        return {
            "message": "Hello Zainab! Welcome to the Campus Idea Board!"
        }

    @app.get("/api/ideas")
    def get_ideas() -> list[Idea]:
        return store.find_all()

    @app.post("/api/ideas", status_code=201)
    def create_idea(request: IdeaRequest) -> Idea:
        try:
            return store.add(request)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Title and category are required"
            )

    return app


app = create_app()
