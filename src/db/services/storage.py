"""
    Файл с функциями взаимодействий с local_storage.
"""

from ..models import Group, Main_Page, Key
from src.db import local_storage
from .group import find_all_groups
from .main_page import (get_main_page_hash, get_main_page_info_struct)
from src.utils import logger


async def check_update():
    h = await get_main_page_hash()
    if await local_storage.get(Key("main_page_hash")) != h:
        await initialize_storage()
        await local_storage.put(Key("main_page_hash"), h)


async def initialize_storage():
    """
        Загрузка некоторых данных из бд в программу.
        (ensure_indexes требуется для работы umongo)
    """
    await Group.ensure_indexes()
    await Main_Page.ensure_indexes()
    names_list, all_groups = await find_all_groups()
    info, struct = await get_main_page_info_struct()
    await local_storage.put(Key("groups_all"), all_groups)
    await local_storage.put(Key("groups_list"), names_list)
    await local_storage.put(Key("groups_structure"), struct)
    await local_storage.put(Key("updates"), info)
    await local_storage.put(Key("main_page_hash"), await get_main_page_hash())
    logger.info("Storage initialized.")
