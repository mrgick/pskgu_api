"""
    Апи для класса главной страницы
"""

from src.db import local_storage
from src.db.models import Key
from src.db.services import check_update


async def get_updates(last):
    await check_update()
    info = await local_storage.get(Key("updates"))
    if last:
        key = list(info)[-1]
        return {key: info[key]}
    else:
        return info
