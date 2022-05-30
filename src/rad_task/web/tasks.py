import aiohttp_sqlalchemy as ahsa
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
            return json_response([to_dict(task) for task in tasks.scalars()])

    async def post(self):
        """
        ---
        description: This endpoint adds tasks to the list
        tags:
        - Task
        produces:
        - application/json
        responses:
            "201":
                description: successful operation. Show the task created
            "405":
                description: invalid HTTP Method
            "400":
                description: invalid input data
        """
        db_session = self.get_sa_session()
        data = await self.request.json()

        async with db_session.begin():
            task = Task(**data)
            db_session.add(task)
            await db_session.commit()

        return json_response(to_dict(task), status=201)


def to_dict(task: Task) -> dict:
    """Transform task to dict"""
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
    }
