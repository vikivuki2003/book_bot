from copy import deepcopy
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from database.database import user_dict_template, users_db
from filters.filters import IsDelBookmarkCallbackdata, IsDigitCallbackdata
from keyboards.bookmarks_kb import create_bookmarks_keyboard
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon_ru import LEXICON
from services.file_handling import book

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    user_id = message.from_user.id
    if user_id not in users_db:
        users_db[user_id] = deepcopy(user_dict_template)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    user_id = message.from_user.id
    if user_id not in users_db:
        return await message.answer("Пользователь не найден.")

    users_db[user_id]['page'] = 1
    text = book[users_db[user_id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[user_id]["page"]}/{len(book)}',
            'forward'
        )
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    user_id = message.from_user.id
    if user_id not in users_db:
        return await message.answer("Пользователь не найден.")

    page = users_db[user_id].get('page', 1)
    text = book[page]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{page}/{len(book)}',
            'forward'
        )
    )


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    user_id = message.from_user.id
    if user_id not in users_db:
        return await message.answer("Пользователь не найден.")

    bookmarks = users_db[user_id].get("bookmarks", [])
    if bookmarks:
        await message.answer(
            text=LEXICON[message.text],
            reply_markup=create_bookmarks_keyboard(*bookmarks)
        )
    else:
        await message.answer(text=LEXICON['no_bookmarks'])


@router.callback_query(F.data == 'forward')
async def process_forward_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in users_db:
        return await callback.answer("Пользователь не найден.")

    if users_db[user_id]['page'] < len(book):
        users_db[user_id]['page'] += 1
        text = book[users_db[user_id]['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[user_id]["page"]}/{len(book)}',
                'forward'
            )
        )
    await callback.answer()
