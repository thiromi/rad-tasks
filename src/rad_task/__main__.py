from aiohttp import web
from aiohttp_swagger import setup_swagger

from .web.tasks import routes as task_routes

if __name__ == "__main__":
    app = web.Application()
    app.router.add_routes(task_routes)
    setup_swagger(app, swagger_url="/api/docs", ui_version=2)
    web.run_app(app)
