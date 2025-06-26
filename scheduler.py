import asyncio
from database import cleanup_expired_tokens

def cleanup_tokens_job():
    async def job():
        while True:
            await cleanup_expired_tokens()
            await asyncio.sleep(300)
    asyncio.get_event_loop().create_task(job())