"""
    Апи для класса главной страницы
"""

from src.db import local_storage
from src.db.models import Key


async def get_updates(last):
    info = await local_storage.get(Key("updates"))
    if last:
        key = list(info)[-1]
        return {key: info[key]}
    else:
        return info
