import requests
import asyncio
from main.bot import dp, bot

async def run_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())