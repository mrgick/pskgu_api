"""
    Апи для класса главной страницы
"""

from src.db.services.main_page import get_main_page_information


async def get_updates(last):
    info = await get_main_page_information()
    if last:
        key = list(info)[-1]
        return {key: info[key]}
    else:
        return info
