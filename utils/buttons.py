from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def sub_channel_button(not_subscribed):
    buttons = [InlineKeyboardButton(text=f"{idx+1}-kanal", url=f"https://t.me/{channel}") for idx, channel in enumerate(not_subscribed)]
    buttons.append(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check"))
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard