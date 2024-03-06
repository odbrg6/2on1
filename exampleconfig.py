from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

class Config:
    # قم بإضافة المتغيرات اللازمة هنا
    APP_ID = os.environ.get("APP_ID", "24574525")
    APP_HASH = os.environ.get("APP_HASH", "d9c4c2459f68da63c58517e431d49149")
    SESSION = os.environ.get("SESSION", "")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", "")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", ".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", ".")

olgaly = TelegramClient(StringSession(Config.SESSION), Config.APP_ID, Config.APP_HASH)
