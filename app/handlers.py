from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from config import bot, admin_chat_id
from states import FeedbackStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Выберите регион.", reply_markup=kb.main)


@router.callback_query(F.data == 'feedback')
async def feedback_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, введите ваш отзыв:")
    await state.set_state(FeedbackStates.waiting_for_feedback)


@router.message(FeedbackStates.waiting_for_feedback)
async def feedback_received(message: Message, state: FSMContext):
    await bot.send_message(admin_chat_id, f"Новое сообщение от @{message.from_user.username}:\n\n{message.text}")
    await message.answer("Спасибо за ваш отзыв!")
    await state.clear()
@router.callback_query(F.data == "regions")
async def choose_regions(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text="Регионы", reply_markup=kb.kb_regions)

@router.callback_query(F.data == 'categories')
async def choose_categories(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Категории:', reply_markup=kb.kb_categories)

@router.callback_query(F.data == "master-class")
async def master_class(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:1)ссылка на бота для выбора другого '
                                          'канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;', reply_markup=kb.master_class)

@router.callback_query(F.data == "tournaments")
async def tournaments(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:1)ссылка на бота для выбора другого '
                                          'канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;\n3) ссылка на канал для поиска попутчиков __________;', reply_markup=kb.tournaments)

@router.callback_query(F.data == "find_partner")
async def find_partner(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='канал с возможностью комментировать посты; '
                                          '\nпосты размещают участники канала через бота Описание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления перейдите к боту - _______;', reply_markup=kb.find_partners)

@router.callback_query(F.data == "clothes")
async def clothes(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='канал с возможностью комментировать посты; '
                                          'посты размещают участники канала через бота\nОписание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления перейдите к боту - _______;\n3)ссылка на канал 7.Обувь б/у: __________.', reply_markup=kb.clothes)

@router.callback_query(F.data == "second_shoes")
async def choose_regions(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='канал с возможностью комментировать посты; '
                                          'посты размещают участники канала через бота\nОписание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления перейдите к боту - _______;\n3)ссылка на канал 8.Одежда б/у: __________.', reply_markup=kb.shoes)

@router.callback_query(F.data == "companion")
async def companion(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='канал с возможностью комментировать посты; '
                                          'посты размещают участники канала через бота\nОписание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления перейдите к боту - _______;', reply_markup=kb.companies)

@router.callback_query(F.data == "find_room")
async def find_room(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;', reply_markup=kb.find_room)

@router.callback_query(F.data == "pro-am")
async def pro_am(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;', reply_markup=kb.pro_am)

@router.callback_query(F.data == "shop")
async def shop(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;', reply_markup=kb.shop)

@router.callback_query(F.data == "work")
async def work(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='канал с возможностью комментировать посты; посты размещают участники канала через бота\nОписание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления перейдите к боту - _______;', reply_markup=kb.work)

@router.callback_query(F.data == "clubs")
async def clubs(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Описание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) для размещения объявления обращаться к админу - _______;', reply_markup=kb.clubs)

@router.callback_query(F.data == "forums")
async def forums(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='ГРУППА с подгруппами, чат\nОписание:\n1)ссылка на бота для выбора другого канала/региона ________;\n2) Правила... Общаться только о танцах; немедленный БАН за ругательства, политические высказывания, непристойные картинки/фото', reply_markup=kb.forums)