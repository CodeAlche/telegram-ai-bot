import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from openai import OpenAI

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🤖 AI Bot is live!")

@dp.message()
async def chat(message: Message):
    await bot.send_chat_action(message.chat.id, "typing")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": message.text}]
    )

    reply = response.choices[0].message.content
    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
