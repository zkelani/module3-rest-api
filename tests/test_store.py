import pytest
from app.models import IdeaRequest
from app.store import IdeaStore


def test_fresh_store_is_empty(tmp_path):
    store = IdeaStore(tmp_path / "test.db")
    assert len(store.find_all()) == 0


def test_adding_idea_stores_title_and_category(tmp_path):
    store = IdeaStore(tmp_path / "test.db")

    request = IdeaRequest(
        title="Start a robotics club",
        category="clubs"
    )

    idea = store.add(request)

    assert idea.title == "Start a robotics club"
    assert idea.category == "clubs"

    all_ideas = store.find_all()
    assert len(all_ideas) == 1
    assert idea in all_ideas


def test_two_new_ideas_receive_different_ids(tmp_path):
    store = IdeaStore(tmp_path / "test.db")

    request1 = IdeaRequest(
        title="Start a robotics club",
        category="clubs"
    )

    request2 = IdeaRequest(
        title="Create a study group",
        category="education"
    )

    idea1 = store.add(request1)
    idea2 = store.add(request2)

    assert idea1.id != idea2.id
    assert idea1.id > 0
    assert idea2.id > 0
    assert len(store.find_all()) == 2


def test_idea_persists_after_reopening_store(tmp_path):
    db_path = tmp_path / "persistence.db"

    store = IdeaStore(db_path)

    created = store.add(
        IdeaRequest(
            title="Start a coding club",
            category="clubs"
        )
    )

    reopened_store = IdeaStore(db_path)
    saved_ideas = reopened_store.find_all()

    assert len(saved_ideas) == 1
    assert saved_ideas[0].id == created.id
    assert saved_ideas[0].title == created.title
    assert saved_ideas[0].category == created.category