from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from RAUSHAN.db.users import add_served_user, get_served_users

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(client, msg: Message):
    served_users = await get_served_users()
    is_new_user = msg.from_user.id not in served_users
    await add_served_user(msg.from_user.id)
    if is_new_user:
        # Notify only the bot owner, only for first-time users
        try:
            await client.send_message(chat_id=OWNER_ID, text=f"New user started the bot: {msg.from_user.id}")
        except Exception:
            # Don't let a failed notification break message handling for the user
            pass

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)
