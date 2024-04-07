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
API_ID = config("23858329", default=None, cast=int)
API_HASH = config("e2cd67ed2be80b60b52ff80fc3e6c127", default=None)
BOT_TOKEN = config("7079907278:AAFcj7FbASiJjU7m9DVI6-H3jMaR86QADo0", default=None)
SESSION = config("BQFsDJkAPzkzlefaqkTq_Py2BCs9DksLSrIPwuz3uEoEr1PQ8hNo3cUMmRRvNsU5SVMWineZa1GVNFLcXhH4SQQRJKJ1EXV0kNQSGe4JAmUDxyBmGDNP0rtxoVPA_d1noH9JhiqJ0_b_Dd7qlryUqVcKal04YJdyJgMJr5t4e2Oif0BOoBLB9ngdeOee-Ox0yDeZlrzWkNQPtoRD9ZVff23Gt4oqcfABtobGBB9ARxJxb6MFDjhiDH4VMA8mo02Lc3ctW3DuQwMUQkklEpliuLRoMx_8QbVsgCA8DG1yo8RCOzW2g1USAyfsYHAXBM9ElK1y0cgYvyTToanaqRgMvnrBjvRJ1AAAAAFOjqOBAA", default=None)
FORCESUB = config("SaveByAspirant", default=None)
AUTH = config("5612938113", default=None)
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
