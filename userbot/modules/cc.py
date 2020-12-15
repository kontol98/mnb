
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register

@register(outgoing=True, pattern="^\/cc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@cc_pebot"
    chk = f"chk"
    await event.edit("```Processing```")
    async with bot.conversation("@cc_pebot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1370126606))
              await conv.send_message(f'!{chk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @cc_pebot plox```")
              return
          else:
             await event.edit(f"{response.message.message}")
             await bot.send_read_acknowledge(conv.chat_id)
