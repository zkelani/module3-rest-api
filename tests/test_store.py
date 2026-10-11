import pytest
from app.models import IdeaRequest
from app.store import IdeaStore

def test_fresh_store_contains_two_seed_ideas():
    # A unit test: no web server or HTTP client.
    store = IdeaStore()
    assert len(store.find_all()) == 2


def test_adding_idea_stores_title_and_category():
    store = IdeaStore()

    request = IdeaRequest(
        title="Start a robotics club",
        category="clubs"
    )

    idea = store.add(request)

    assert idea.title == "Start a robotics club"
    assert idea.category == "clubs"

    all_ideas = store.find_all()
    assert len(all_ideas) == 3
    assert idea in all_ideas

def test_two_new_ideas_receive_different_ids():
    store = IdeaStore()

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
    assert idea1.id not in [1, 2]
    assert idea2.id not in [1, 2]
    assert len(store.find_all()) == 4