from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.text(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user message.")
        return
    reply_message = await event.get_reply_message()
    # if not reply_message.text:
    # await event.edit("
reply to text message
")
    # return
    chat = "@SmartFileUtilsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    await event.edit("Scanning...")
    async with bot.conversation(chat) as conv:
        try:
            r1 = await conv.get_response()
            r2 = await conv.get_response()
            await bot.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply("Please unblock   and try again")
            return
        if r1.text.startswith("Forward"):
            await event.edit("can you kindly disable your forward privacy settings for good?")
        else:
            await event.edit(f"{r2.message.message}")


CMD_HELP.update({
    "text":
        ".text \
          \n image to text .\n"
})
