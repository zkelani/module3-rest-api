from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models import Idea, IdeaRequest
from app.store import IdeaStore

def create_app() -> FastAPI:
    app = FastAPI(title="Campus Idea Board")
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    )
    store = IdeaStore()  # Fresh store per app; test clients can be isolated.

    # FastAPI normally uses 422 for validation errors. We supply this handler
    # so both classroom tracks use the same 400 error contract.
    @app.exception_handler(RequestValidationError)
    async def invalid_request(request: Request, error: RequestValidationError):
        return JSONResponse(status_code=400, content={"message": "Invalid request"})

    @app.get("/api/hello")
    def hello():
        # TODO 1: Personalize the message; keep the "message" key.
        return {"message": "Hello Zainab! Welcome to the Campus Idea Board!"}

    @app.get("/api/ideas")
    def get_ideas() -> list[Idea]:
        return store.find_all()

    @app.post("/api/ideas", status_code=201)
    def create_idea(request: IdeaRequest) -> Idea:
        return store.add(request)

    return app

app = create_app()
