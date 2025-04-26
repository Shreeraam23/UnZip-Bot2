# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client
from Unzip.config import Config
import os

app = Client(
    "unzip_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="Unzip")
)
port = int(os.environ.get("PORT", 8080))
server = HTTPServer(('0.0.0.0', port), Handler)

print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
app.run()
