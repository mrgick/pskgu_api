"""
    Апи для класса групп
"""
from fastapi import HTTPException
from src.db.models import Key
from src.db import local_storage


async def get_groups(list_of_names, name):
    if list_of_names:
        return await get_all_list_of_groups(list_of_names)
    if name:
        return await get_info_of_one_group(name)
    raise HTTPException(status_code=400,
                        detail="No parameters. One of them must be.")


async def get_all_list_of_groups(name):
    if name == "list":
        groups = await local_storage.get(Key("groups_list"))
    elif name == 'structure':
        groups = await local_storage.get(Key("groups_structure"))
    else:
        raise HTTPException(status_code=400,
                            detail="Error arguments. " +
                            "No arg with list_of_names=" + name)
    return {"list_of_names": groups}


async def get_info_of_one_group(name):
    if name == "all":
        return await local_storage.get(Key("groups_all"))
    else:
        group = (await local_storage.get(Key("groups_all"))).get(name)
        if group:
            return group
    raise HTTPException(status_code=404, detail="No group with name=" + name)
