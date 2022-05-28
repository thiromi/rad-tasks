import aiohttp_sqlalchemy as ahsa
import sqlalchemy as sa
from aiohttp import web
from aiohttp.web_response import json_response
from sqlalchemy.future import select

from rad_task.domain.tasks import Task

routes = web.RouteTableDef()


@routes.view("/api/tasks")
class TaskView(web.View, ahsa.SAMixin):
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
        db_session = self.get_sa_session()

        async with db_session.begin():
            tasks = await db_session.execute(select(Task))
            return json_response([task.to_dict() for task in tasks.scalars()])

    async def post(self):
        return web.Response(text="Post")
