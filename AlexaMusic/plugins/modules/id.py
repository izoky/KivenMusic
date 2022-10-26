# Alexa

from AlexaMusic import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ايديك**: `{message.from_user.id}`\n**{reply.from_user.first_name}'ايدي المستخدم**: `{reply.from_user.id}`\n**ايدي الدردشة**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ايديك**: `{message.from_user.id}`\n**ايدي الدردشة**: `{message.chat.id}`"
        )
