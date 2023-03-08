import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23640300"))
    API_HASH = os.environ.get("API_HASH", "b43066e201bfc457ad566e623fd74dab")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6243903054:AAGxLIvpbt_v9oySQG2FZ14HVvfSO2cI6I4")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5149183428")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://projectnv:projectnv321@cluster0.wieiqcz.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001885467323"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@nancyB_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
