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
        else:
            downloaded_file_name = await event.client.download_media(
                                 response.media,
                                 TEMP_DOWNLOAD_DIRECTORY
            )
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
            )
            """ - cleanup chat after completed - """
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
    await event.delete()
    return os.remove(downloaded_file_name)
