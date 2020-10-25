from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

@register(outgoing=True, pattern=r"^\.nulis(?: |$)(.*)")
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
            await event.reply("Unblock @Rajinnulis12_bot plox")
            return
        await conv.send_message(reply_message)
            r1 = await conv.get_response()
        except YouBlockedUserError:
            await event.reply("Please unblock   and try again")
            return
        if r1.text.startswith("Forward"):
            return await event.edit("can you kindly disable your forward privacy settings for good?")
        elif r1.text.startswith("Harap Tunggu, Bot Sedang Menulis Buku 1!~"):
            r2 = await conv.get_response()
            await event.edit(f"{r2.message}")
        else:
            return await event.edit("Bug lol!")
