from aiohttp import web

from src.rad_task.web.app import create

if __name__ == "__main__":
    web.run_app(create())
