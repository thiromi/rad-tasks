import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient

from rad_task import config
from rad_task.web.app import create


@pytest.fixture(autouse=True)
def config_app():
    """All changes to the app config should be done here"""
    config.DB_STRING = "sqlite+aiosqlite:///"


@pytest.fixture
async def app() -> web.Application:
    return await create()


@pytest.fixture
async def client(aiohttp_client, app: web.Application) -> TestClient:
    return await aiohttp_client(app)
