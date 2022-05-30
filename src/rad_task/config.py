import os
from pathlib import Path

BASEDIR = Path(os.path.dirname(os.path.abspath(__file__)))

DB_STRING = os.environ.get(
    "DB_STRING", "postgresql+asyncpg://raduser:radpass@postgres:5432/rad_task"
)

TEMPLATES_FOLDER = BASEDIR / "web" / "templates"
