import aiohttp_jinja2
from aiohttp import web

routes = web.RouteTableDef()


@routes.view("/")
@aiohttp_jinja2.template("task.jinja2")
async def index(request):
    return {}
