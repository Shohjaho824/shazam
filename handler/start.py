from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.sub import check_subscriptions, CHANNELS


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    """
    asosiy start handleri
    """
    user_id = message.from_user.id
    is_subchannel = await check_subscriptions(user_id)

    if not is_subchannel:
        first_name = message.from_user.first_name
        await message.answer(texts.START.format(first_name))
    else:
        await message.answer(
            texts.NOT_CHANNEL, 
            reply_markup=buttons.sub_channel_button(is_subchannel))