"""
    Настроки апи
"""

import os


class Config:
    """
        Класс настроек
    """
    # настройки cron
    CRON_PERIOD = 5*60
    URL_PING = os.environ.get('URL_PING')

    # настроки mongo db
    DB_NAME = "DB"
    MAX_POOL_SIZE = 10
    MONGO_URI = os.environ.get('MONGO_URL')
