"""
    Файл с функциями взаимодействий с классом Group.
"""

from db.models import Group, Key
from db import local_storage


async def find_all_groups():
    """
        Находит все имена групп и преподавателей.
    """
    return [x.name async for x in Group.find()]


async def find_group_by_name(name):
    """
        Находит одну группу или преподавателя.
    """
    if name in await local_storage.get(Key("groups")):
        return await Group.find_one(filter={"name": name})
    return None
