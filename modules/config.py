# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "7f10cf5e8390a3ff33c7bbc581469984")
API_ID = int(getenv("API_ID", "9620148"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏")
ASSISTANT_USERNAME = getenv("brokenx_Assistant", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/c1fcb2141ba17c3ca7e46.jpg")
BOT_NAME = getenv("BOT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_TOKEN = getenv("BOT_TOKEN", "5572910868:AAFvZUZQEEUp2KVbCOsIMjnutNPFZauu9zo")
BOT_USERNAME = getenv("BROKENXZE_VCBOT", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "- ❛𝗠𝘁𝘀 ➻ 𝗕𝗿𝗼𝗸𝗲𝗻 𝗕𝗼𝘆 [🇮🇳]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "B_R_O_K_E_N_BOY")
SOURCE_CODE = getenv("SOURCE_CODE", "https://")
STRING_SESSION = getenv("STRING_SESSION", "BQAX11EnqXaiyILOl1qbWGow16YrJmkpzJRwy_Vawd2p-hquQsjuFJTMGvzxwgfY2tdTnDPTiyuXCf5Ini8lHB6pAfPl8FQwgJE3IVjMe4phEK9aRjByh4g_F9AsPwY2_iFYhE4YisZk-1n3LX4rmq4oTEv5eotIIQ85N2jsmgpE8fJDh-U0VXkbW5Z5UF6blNsscSvY7U4CdS4iUM5_7CzDAW676pLJKLSgmspyLx9_u0iHFoakvXM3xKkUVydRQi4QtncTg2_3fAy_H1JgRWokuz9zyO8fLYGDwn0z6AvG3YsnVss1QQvI2tv-FgAsGD9wtUNLfOow2ljmL7vLpOpuAAAAAUBfQeEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5374951905").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/MYSTERIOUS_CHATS")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RTH_FIGHTERS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/kaalxd")
