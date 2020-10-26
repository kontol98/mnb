import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register
 
@register(outgoing=True, pattern="^\.nulis(?: |$)(.*)")
async def _(nulis):
    if event.fwd_from:
        return
    link = nulis.pattern_match.group(1)
    chat = "@Rajinnulis12_bot"
    magernulis1 = f"magernulis1"
    await nulis.edit("
Processing
")
    async with bot.conversation("@Rajinnulis12_bot") as conv:
          try:
              response = conv.wait_nulis(events.NewMessage(incoming=True,from_users=1347432560))
              await conv.send_message(f'/{magernulis1} {link}')
              response = await response
          except YouBlockedUserError:
              await nulis.reply("
Unblock @scriptkiddies_bot plox
")
              return
          else:
             await nulis.edit(f"{response.message.message}")
