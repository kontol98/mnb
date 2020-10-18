import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register
 
@register(outgoing=True, pattern="^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"
    nmap = f"nmap"
    await event.edit("```Processing```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=510263282))
              await conv.send_message(f'/{nmap} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.edit(f"{response.message.message}")
