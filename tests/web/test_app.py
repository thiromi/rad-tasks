import pytest
from aiohttp import web

from rad_task.web.app import create


@pytest.fixture
async def app() -> web.Application:
    return await create()


def test_create_returns_application_object(app: web.Application):
    assert isinstance(app, web.Application)


def test_create_setup_docs(app: web.Application):
    assert [
        route
        for route in app.router.routes()
        if route.resource.canonical == "/api/docs"
    ]
