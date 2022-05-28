import pytest

from rad_task import config


@pytest.fixture(autouse=True)
def config_app():
    """All changes to the app config should be done here"""
    config.DB_STRING = "sqlite+aiosqlite:///"
