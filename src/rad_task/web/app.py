from aiohttp import web
from aiohttp_swagger import setup_swagger

from rad_task.web.tasks import routes as task_routes


def create() -> web.Application:
    """Creates the web.Application for the entrypoint"""
    app = web.Application()
    app.router.add_routes(task_routes)
    setup_swagger(app, swagger_url="/api/docs", ui_version=2)

    return app
