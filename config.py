from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24478892")
    API_HASH = environ.get("API_HASH", "b7b00353625f83dbf6ca2438353515a0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7042426390:AAHm0OOyDf4Tl3ajJF5Eu8CX_0SecUeqpyg") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQF1hKwAspsV8GyCWHOsUcU-qJ2aqfANPRUNqv_3ut5h2rJLr1S2fhosqhP22kAVPUyDRhK3TPqLAt-i_vibNu_bsuzBY0YbnopOrbfGPlZLdA669yETyMNYC52ZHv6xO50GV8zjV6MeoYzogvJgNzaJaGl65mGGXDWQOJTbrlf4h3-dFH2hM2cItpP1GKTOa6QufM3e93UHZvYwz_RrFJJh38y82_u-EmkNhQ53ZLkaScwlerTAn3mGBOR0BRL8cp0w0pMDvMwvY8LZVGVNwPOMP6KIOf62xVuofByvE4eOJ1tnyXW3ZfHx9qx5nHKDxavbyyayrHArB1k1e98PP314tKE7eAAAAABFJ2WxAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6585878012').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
