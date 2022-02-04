"""
    Файл с функциями взаимодействий с классом Group.
"""

from ..models import Group, Key
from src.db import local_storage


async def find_all_groups():
    """
        Находит все имена групп и преподавателей.
    """
    all_groups = [x async for x in Group.find()]
    names = []
    groups = {}
    for group in all_groups:
        group = group.dump()
        group.pop("id", None)
        names.append(group['name'])
        groups.update({group['name']: group})
    return (names, groups)
