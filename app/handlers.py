from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from random import randint
from app.generator import gen

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"✋🏻 Привет, шеф {message.from_user.first_name}!\n"
        f"Этот бот поможет тебе в приготовлении любых блюд.\n"
        f"Просто отправь <b>описание того что ты хочешь приготовить</b> - "
        f"бот выдаст тебе <b>подробный рецепт.</b>"
    )


@user.message(F.text)
async def handle_message(message: Message):
    content = message.text
    await message.answer(
        f"✅ <b>Принято!</b>\n"
        f"♻️ Рецепт почти у тебя! Время ожидания: ~ <b>{randint(20, 25)} секунд.</b>\n"
    )

    answer = await gen(content)
    await message.answer(answer)
