from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/725fa8c7b8fc5831d0c23.jpg"
  

          
rizoel = "✧ 𝐊𝐀𝐀𝐋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝐊𝐀𝐀𝐋𝐒𝐏𝐀𝐌𝐁𝐎𝐓 ᴠᴇʀsɪᴏɴ**  : `{kaalversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/KAALNETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TEAM_KAAL_RIDER")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/garwmishra/kaal_spam_bot")
        ]
        ]
        )
    
