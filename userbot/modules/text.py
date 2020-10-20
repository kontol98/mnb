from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def _(text):
    if text.fwd_from:
        return
    if not text.reply_to_msg_id:
        await text.edit("```Reply to any user message.```")
        return
    chat = "@SmartFileUtilsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await text.edit("Reply to actual users message.")
        return
    await text.edit("Scanning")
    async with bot.conversation(chat) as conv:
        try:
            r1 = await conv.get_response()
            r2 = await conv.get_response()
            await bot.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await text.reply("Please unblock   and try again")
            return
        if r1.text.startswith("Forward"):
            await text.edit("can you kindly disable your forward privacy settings for good?")
        else:
            await text.edit(f"
{r2.message.message}
")


CMD_HELP.update({
    "text":
        ".text \
          \n image to text .\n"
})
