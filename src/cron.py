"""
    Cron - постоянное повторение.
"""
import asyncio
import logging
from src.config import Config
from src.db.services import check_update

logger = logging.getLogger(__name__)


async def running():
    while True:
        try:
            await check_update()
        except Exception as e:
            logger.error(e)
        finally:
            await asyncio.sleep(Config.CRON_PERIOD)


async def run_cron():
    loop = asyncio.get_event_loop()
    loop.create_task(running())
    logger.info("Cron launched.")
