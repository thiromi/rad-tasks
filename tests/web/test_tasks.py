import aiohttp_sqlalchemy as ahsa
import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient

from rad_task.domain.tasks import Task


@pytest.fixture
async def db_session(aiohttp_client, app: web.Application) -> ahsa.Session:
    async with ahsa.get_session_factory(app)() as session:
        async with session.begin():
            session.add(Task(title="Test Task", description="test task"))
            await session.flush()
            yield session
            await session.rollback()


async def test_list_tasks_returns_200(client: TestClient):
    resp = await client.get("/api/tasks")
    assert resp.status == 200


async def test_list_tasks_returns_json(client: TestClient):
    resp = await client.get("/api/tasks")
    assert "application/json" in resp.headers["Content-Type"]


async def test_list_tasks_returns_task(
    client: TestClient, app: web.Application, db_session: ahsa.Session
):
    resp = await client.get("/api/tasks")
    assert await resp.json() == [
        {
            "id": 1,
            "title": "Test Task",
            "description": "test task",
            "done": False,
        },
    ]
