#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("24478892", default=None, cast=int)
API_HASH = config("b7b00353625f83dbf6ca2438353515a0", default=None)
BOT_TOKEN = config("7042426390:AAHm0OOyDf4Tl3ajJF5Eu8CX_0SecUeqpyg", default=None)
SESSION = config("BQF1hKwAspsV8GyCWHOsUcU-qJ2aqfANPRUNqv_3ut5h2rJLr1S2fhosqhP22kAVPUyDRhK3TPqLAt-i_vibNu_bsuzBY0YbnopOrbfGPlZLdA669yETyMNYC52ZHv6xO50GV8zjV6MeoYzogvJgNzaJaGl65mGGXDWQOJTbrlf4h3-dFH2hM2cItpP1GKTOa6QufM3e93UHZvYwz_RrFJJh38y82_u-EmkNhQ53ZLkaScwlerTAn3mGBOR0BRL8cp0w0pMDvMwvY8LZVGVNwPOMP6KIOf62xVuofByvE4eOJ1tnyXW3ZfHx9qx5nHKDxavbyyayrHArB1k1e98PP314tKE7eAAAAABFJ2WxAA", default=None)
FORCESUB = config("trygagan", default=None)
AUTH = config("6585878012", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
