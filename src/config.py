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

    # настроки mongo db
    DB_NAME = "DB"
    MAX_POOL_SIZE = 10
    MONGO_URI = os.environ.get('MONGO_URL')
