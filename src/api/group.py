"""
    Апи для класса групп
"""
from fastapi import HTTPException
from src.db.services.main_page import get_main_page_hash
from src.db.services.group import find_group_by_name
from src.db.services import initialize_storage
from src.db.models import Key
from src.db import local_storage


async def get_groups(list_of_names, name):
    if list_of_names or name == "all":
        return await get_all_list_of_groups()
    if name:
        return await get_info_of_one_group(name)
    raise HTTPException(status_code=400,
                        detail="No parameters. One of them must be.")


async def get_all_list_of_groups():
    h = await get_main_page_hash()
    if await local_storage.get(Key("main_page_hash")) != h:
        await initialize_storage()
        await local_storage.put(Key("main_page_hash"), h)
    groups = await local_storage.get(Key("groups"))
    return {"groups_list": groups}


async def get_info_of_one_group(name):
    group = await find_group_by_name(name)
    if group:
        group = group.dump()
        group.pop("id", None)
        return group
    raise HTTPException(status_code=404, detail="No group with name=" + name)
