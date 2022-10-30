# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# تعديل تعريب aditor © @AA37A عبدالله © Rocks 2022
# Owner Asad Ali + Harshit Sharma + Abhimanyu Singh + Krishna Ki Diwani
# حقوق محفوضة مع وجود المنشئ 

import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond(" **أهلا وسهلا كنت بانتضارك** 👋")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ انا بوت كيڤن لعمل تاكات لأعضاء مجموعتك\n✪    لتعرف كيفية استخدامي`/help` انا سعيد لأستخدامك لي ارسل ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ المطور   : [Kiven](https://t.me/AA37A)\n┣★ التحديثات › : [Kiven Bot](https://t.me/kivenbots)┓\n┣★ قناة البوت › : [here](https://t.me/YYN4Y)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 اذا كنت بحاجة الى مساعدة\n قم بارسال رسالة الي  [ᴏᴡɴᴇʀ](https://t.me/T6ooBot) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,a
        buttons=(
            [
                Button.url(
                    "☀︎︎️اضغط هنا لأضافتي☀︎︎",
                    "https://t.me/AA7sbot?startgroup=true",
                ),
            ],
            [
                Button.url("☀︎︎ قناة البوت☀︎︎︎", "https://t.me/YYN4Y"),
                Button.url("☀︎︎ التحديثات والمزيد ☀︎︎", "https://t.me/kivenbots"),
            ],
            [
                Button.url("☀︎︎ عبدالله ☀︎︎️️", "https://t.me/AA37A"),
                Button.url("☀︎︎ بوت تواصل ☀︎︎︎", "https://t.me/T6ooBot"),
            ],
        ),
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond(" حبيبي اطلق من يضغط start 🥺")
    helptext = "✪ اليك قائمة \n\n✪ الأوامر: /mentionall\n✪ لعمل تاك للجميع: /cancel لأيقاف التاكات.\n✪ امر /admin لعمل تاك لجميع المشرفين في المجموعة (لا تلح بهذا الأمر حتى ميطردوك 😂🤍) \n✪ تكدر تخلي. رسالة وية الأمر ويرسلهة وية التاك.\n✪ `مثال: /mentionall صباح الخير!`\n✪ تكدر تستعمل الامر على اي رسالة بلرد عليهة وية الأمر."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ قناة البوت", "https://t.me/YYN4Y"),
                Button.url("التحديثات والمزيد☀︎︎", "https://t.me/kivenbots"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("اهلا وسهلا المطور")
    helptext = "✪ انا بوت كيڤن\n\n✪ مطوري هوة [Abdullah](https://t.me/AA37A)\n✪ القناة الرسمية للتحديثات\n✪ تليكرام [ᴄʜᴀɴɴᴇʟ](https://t.me/kivenbots)\n✪ يسعدني انضمامكم."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ التحديثات ", "https://t.me/kivenbots"),
                Button.url("المطور ☀︎︎", "https://t.me/AA37A"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)__"
            )
    else:
        return await event.respond(
            "__ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("__There is no proccess on going...__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped.__")


print(">> Kiven WORKING <<")
client.run_until_disconnected()


# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Harshit Sharma + Abhimanyu Singh + Krishna Ki Diwani
