import os 
import requests
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command

from config.token import API_TOKEN

# Obyekt Bot
bot = Bot(token=API_TOKEN)

# Dispatcher
dp = Dispatcher()

@dp.message(F.text.lower() == "musiqani qidirish")
async def search_music(message: types.Message):
    await message.answer("Musiqani nomini yozing...")
@dp.message(F.text.lower() == "Qo'shiqchi qidirish")
async def search_artist(message: types.Message):
    await message.answer("Musiqani nomini yozing...")