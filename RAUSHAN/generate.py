from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**☞︎︎︎ ᴄʜᴏᴏsᴇ ᴏɴᴇ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 𖤍 ✔️ **"
buttons_ques = [
    [
        InlineKeyboardButton("▪️ᴘʏʀᴏɢʀᴀᴍ▪️", callback_data="pyrogram"),
        InlineKeyboardButton("▪️ᴘʏʀᴏɢʀᴀᴍ ᴠ2▪️", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🔺ᴛᴇʟᴇᴛʜᴏɴ🔺", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("🔸ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ🔸", callback_data="pyrogram_bot"),
        InlineKeyboardButton("🔹ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ🔹", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="🔹ɢᴇɴʀᴀᴛᴇ sᴇssɪᴏɴ🔹", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭"
    else:
        ty = "𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬"
        if not old_pyro:
            ty += " 𝖵2"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ **{ty}** sᴇssɪᴏɴ ɢᴇɴʀᴀᴛᴏʀ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ᴀᴘɪ_ɪᴅ** ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ.\n\nᴄʟɪᴄᴋ ᴏɴ /skip ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ᴀᴘɪ.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝖠𝖯𝖨_𝖨𝖣** ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ, sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "☞︎︎︎ ɴᴏᴡ ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ᴀᴘɪ_ʜᴀsʜ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "☞︎︎︎ » ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ : \nᴇxᴀᴍᴘʟᴇ : `+91 95xxxxxxXX`'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `6810174902:AAGQVElsBPTNe6Rj16miPbCrDGikscfarYY`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash, in_memory=True)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    if not (telethon and is_bot):
        # For telethon bot login, client.start(bot_token=...) below handles connecting.
        await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        await client.disconnect()
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        await client.disconnect()
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        await client.disconnect()
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            await client.disconnect()
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            await client.disconnect()
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                await client.disconnect()
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(two_step_msg):
                    await client.disconnect()
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                await client.disconnect()
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**ᴛʜɪs ɪs ʏᴏᴜʀ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n**ɢᴇɴʀᴀᴛᴇᴅ ʙʏ :[𝐓ᴇᴀᴍ 𝐏ᴜʀᴠɪ](https://t.me/team_secrat_bots) ᴡᴀʀɴɪɴɢ :** ᴅᴏɴᴛ sʜᴀʀᴇ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ᴇᴠᴇɴ ɪғ ᴡɪᴛʜ ʏᴏᴜʀ ɢғ 🏴‍☠️"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except Exception:
        pass
    finally:
        await client.disconnect()
    await bot.send_message(msg.chat.id, "sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ {} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ғᴏʀ ɢᴇᴛᴛɪɴɢ ɪᴛ.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ [𝐀ʟᴘʜᴀ 𝐁ᴀʙʏ](https://t.me/Session_stringgbot)".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True)
        return True
    else:
        return False
