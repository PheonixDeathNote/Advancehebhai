from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23858329")
    API_HASH = environ.get("API_HASH", "e2cd67ed2be80b60b52ff80fc3e6c127")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7079907278:AAFcj7FbASiJjU7m9DVI6-H3jMaR86QADo0") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQFsDJkAPzkzlefaqkTq_Py2BCs9DksLSrIPwuz3uEoEr1PQ8hNo3cUMmRRvNsU5SVMWineZa1GVNFLcXhH4SQQRJKJ1EXV0kNQSGe4JAmUDxyBmGDNP0rtxoVPA_d1noH9JhiqJ0_b_Dd7qlryUqVcKal04YJdyJgMJr5t4e2Oif0BOoBLB9ngdeOee-Ox0yDeZlrzWkNQPtoRD9ZVff23Gt4oqcfABtobGBB9ARxJxb6MFDjhiDH4VMA8mo02Lc3ctW3DuQwMUQkklEpliuLRoMx_8QbVsgCA8DG1yo8RCOzW2g1USAyfsYHAXBM9ElK1y0cgYvyTToanaqRgMvnrBjvRJ1AAAAAFOjqOBAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5612938113').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
