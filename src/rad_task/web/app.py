import traceback

import aiohttp_jinja2
import aiohttp_sqlalchemy as ahsa
import jinja2
from aiohttp import web
from aiohttp_swagger import setup_swagger

from rad_task import config
from rad_task.domain import metadata
from rad_task.web.index import routes as index_routes
from rad_task.web.tasks import routes as task_routes


async def setup_database(app: web.Application):
    """Setup database connection"""
    ahsa.setup(
        app,
        [
            ahsa.bind(config.DB_STRING),
        ],
    )

    await ahsa.init_db(app, metadata)  # TODO: use alembic to create the database


async def create() -> web.Application:
    """Creates the web.Application for the entrypoint"""
    app = web.Application(middlewares=[error_handler])
    app.router.add_routes(task_routes)
    app.router.add_routes(index_routes)
    setup_swagger(app, swagger_url="/api/docs", ui_version=2)
    await setup_database(app)
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(config.TEMPLATES_FOLDER))
    )

    return app


@web.middleware
async def error_handler(request: web.Request, handler):
    """
    Error handler for the application.
    """
    try:
        return await handler(request)
    except web.HTTPException:
        raise
    except Exception as exc:
        return web.json_response(
            {
                "error": str(exc),
                "traceback": "".join(
                    traceback.format_exception(type(exc), exc, exc.__traceback__)
                ),
            },
            status=500,
        )
