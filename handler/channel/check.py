from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from utils.sub import check_subscriptions, CHANNELS

@dp.callback_query_handler(lambda call: call.data == 'check')
async def check(callback: CallbackQuery, state: FSMContext):
    user_id = callback.message.from_user.id
    is_subchannel = await check_subscriptions(user_id)

    if not is_subchannel:
        first_name = callback.message.from_user.first_name
        await callback.message.answer(texts.START.format(first_name))
    else:
        await callback.message.answer(
            texts.NOT_CHANNEL, 
            reply_markup=buttons.sub_channel_button(CHANNELS)
        )



        