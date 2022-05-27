import os

DB_STRING = os.environ.get(
    "DB_STRING", "postgresql+asyncpg://raduser:radpass@localhost:5432/rad_task"
)
