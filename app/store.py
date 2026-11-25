
import os
import sqlite3
from pathlib import Path
from contextlib import closing
from app.models import Idea, IdeaRequest


class IdeaStore:
    """SQLite database store for ideas."""

    def __init__(self, db_path=None):
        self.db_path = Path(
            db_path or os.getenv("DB_PATH", "data/ideas.db")
        )

        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        schema_path = Path(__file__).with_name("schema.sql")

        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.executescript(
                schema_path.read_text(encoding="utf-8")
            )
            conn.commit()

    def find_all(self) -> list[Idea]:
        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row

            rows = conn.execute(
                "SELECT id, title, category FROM ideas ORDER BY id"
            ).fetchall()

            return [Idea(**dict(row)) for row in rows]

    def add(self, request: IdeaRequest) -> Idea:
        title = request.title.strip()
        category = request.category.strip()

        if not title or not category:
            raise ValueError("Title and category are required")

        with closing(sqlite3.connect(self.db_path)) as conn:
            cursor = conn.execute(
                "INSERT INTO ideas (title, category) VALUES (?, ?)",
                (title, category)
            )

            conn.commit()

            return Idea(
                id=cursor.lastrowid,
                title=title,
                category=category
            )