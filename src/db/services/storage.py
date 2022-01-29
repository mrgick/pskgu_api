"""
    Файл с функциями взаимодействий с local_storage.
"""

from ..models import Group, Main_Page, Key
from src.db import local_storage
from .group import find_all_groups
from .main_page import get_main_page_hash
from src.utils import logger


async def initialize_storage():
    """
        Загрузка некоторых данных из бд в программу.
        (ensure_indexes требуется для работы umongo)
    """
    await Group.ensure_indexes()
    await Main_Page.ensure_indexes()
    await local_storage.put(Key("groups"), await find_all_groups())
    await local_storage.put(Key("main_page_hash"), await get_main_page_hash())
    logger.info("Storage initialized.")
