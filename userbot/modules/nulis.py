import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register
 
@register(outgoing=True, pattern="^\.nulis(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Rajinnulis12_bot"
    magernulis1 = f"magernulis1"
    await event.edit("
Processing
")
    async with bot.conversation("@Rajinnulis12_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1347432560))
              await conv.send_message(f'/{magernulis1} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("
Unblock @scriptkiddies_bot plox
")
              return
          else:
             await event.edit(f"{response.message.message}")
