import aiohttp_sqlalchemy as ahsa
from aiohttp import web
from aiohttp.web_response import json_response
from sqlalchemy.future import select

from rad_task.domain.tasks import Task

routes = web.RouteTableDef()


@routes.get("/api/tasks")
async def get(request: web.Request):
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
    db_session = ahsa.get_session(request)

    async with db_session.begin():
        tasks = await db_session.execute(select(Task))
        return json_response([to_dict(task) for task in tasks.scalars()])


@routes.post("/api/tasks")
async def post(request: web.Request):
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
    db_session = ahsa.get_session(request)
    data = await request.json()

    async with db_session.begin():
        task = Task(**data)
        db_session.add(task)
        await db_session.commit()

    return json_response(to_dict(task), status=201)


@routes.delete("/api/tasks/{id}")
async def delete(request: web.Request):
    """
    ---
    description: This endpoint deletes tasks from the list
    tags:
    - Task
    produces:
    - application/json
    responses:
        "204":
            description: successful operation
        "405":
            description: invalid HTTP Method
    """
    db_session = ahsa.get_session(request)
    task_id = int(request.match_info["id"])

    async with db_session.begin():
        query = await db_session.execute(select(Task).where(Task.id == task_id))
        task = query.scalar_one()
        await db_session.delete(task)
        await db_session.commit()

    return json_response(status=204)


@routes.patch("/api/tasks/{id}")
async def patch(request: web.Request):
    """
    ---
    description: This endpoint updates tasks from the list
    tags:
    - Task
    produces:
    - application/json
    responses:
        "200":
            description: successful operation
        "405":
            description: invalid HTTP Method
        "400":
            description: invalid input data
    """
    db_session = ahsa.get_session(request)
    task_id = int(request.match_info["id"])
    data = await request.json()

    async with db_session.begin():
        query = await db_session.execute(select(Task).where(Task.id == task_id))
        task = query.scalar_one()
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.done = data.get("done", task.done)
        await db_session.commit()

    return json_response(to_dict(task))


def to_dict(task: Task) -> dict:
    """Transform task to dict"""
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
    }
