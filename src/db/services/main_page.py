"""
    Файл с функциями взаимодействий с классом Main_Page.
"""

from ..models import Main_Page


async def get_main_page_hash():
    """
        Получение хеша главной страницы.
    """
    main_page = await Main_Page.find_one()
    return main_page.page_hash


async def get_main_page_information():
    """
        Получение информации главной страницы.
    """
    main_page = await Main_Page.find_one()
    return main_page.information
