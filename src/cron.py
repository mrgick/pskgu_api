"""
    Cron - постоянное повторение.
"""

import httpx
import asyncio
import logging
from src.config import Config
from src.db.services import check_update

logger = logging.getLogger(__name__)


async def check_status_site(url):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
    except Exception as e:
        logger.error(e)
        logger.error("Site is not available!")


async def running():
    period = Config.CRON_PERIOD
    url = Config.URL_PING
    if url is None:
        return True
    while True:
        try:
            await check_update()
            await check_status_site(url)
        except Exception as e:
            logger.error(e)
        finally:
            await asyncio.sleep(period)


async def run_cron():
    loop = asyncio.get_event_loop()
    loop.create_task(running())
    logger.info("Cron launched.")
