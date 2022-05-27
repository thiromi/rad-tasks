import pytest
from aiohttp.test_utils import TestClient

from rad_task.web.app import create


@pytest.fixture
async def client(aiohttp_client) -> TestClient:
    return await aiohttp_client(create())


async def test_list_tasks_returns_200(client: TestClient):
    resp = await client.get("/api/tasks")
    assert resp.status == 200
