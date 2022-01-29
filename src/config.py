"""
    Настроки апи
"""

import os


class Config:
    """
        Класс настроек
    """

    # настроки mongo db
    DB_NAME = "DB"
    MAX_POOL_SIZE = 100
    MONGO_URI = os.environ.get('MONGO_URL')