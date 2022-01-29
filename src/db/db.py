"""
    Работа с mongo db.
"""

from config import Config
from motor.motor_asyncio import AsyncIOMotorClient
from umongo.frameworks import MotorAsyncIOInstance
from .local_storage import Storage

mongo_client = AsyncIOMotorClient(Config.MONGO_URI,
                                  maxPoolSize=Config.MAX_POOL_SIZE)
instance = MotorAsyncIOInstance(mongo_client[Config.DB_NAME])
local_storage = Storage()
