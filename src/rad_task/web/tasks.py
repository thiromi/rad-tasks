from aiohttp import web

routes = web.RouteTableDef()


@routes.view("/api/tasks")
class TaskView(web.View):
    async def get(self):
        """
        ---
        description: This endpoint list all tasks
        tags:
        - Task
        produces:
        - application/json
        responses:
            "200":
                description: successful operation. List all tasks
            "405":
                description: invalid HTTP Method
        """
        return web.Response(text="Hello, stranger")

    async def post(self):
        return web.Response(text="Post")
