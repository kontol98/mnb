from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

@register(outgoing=True, pattern=r"^\.wall(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    await event.edit("Processing")
    async with bot.conversation("@Rajinnulis12_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1347432560))
            await conv.send_message(f"/magernulis1 {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @SaitamaRobot plox")
            return
        else:
            await event.edit(f"{response.message.message}
