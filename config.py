import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "10683462"))
    API_HASH = os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680348811:AAFTg0TmzNx6dBPG5A2TQ3meJq3_npGVs2A")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot")
    OWNER_ID = os.environ.get("OWNER_ID", "5685227453")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAbTC5fvQ8gO5e-13Trhkx7P90RpgFdDuHQTvh8l-dHPDsPeBVDNk3LzZdUTRXq6H165CvnhrCxMREHW4Dv9PWdvarZJBr7XBkHbSbcBGJQUyuc9FcFluL7OmzCwTsn2jtcRfWV4Pw80k3N16-9HyZcBu8p22FECsfZfZflZdI5Zz1Z_Q9RoIcTq5UxwK7ofqfZVpCx_8H_FfvmfykdYtBg3kTBajI_5lpnFBGoAzkFO_AdiKUdHldnt8jUP0hpVKACRyaq9vzON7An1vUi_SAYHxCb8abMVX19nVoEEh01_HuGk0Fj42JL0O_p7wudlM7bHhMfAIUemj-BcOA8R23yAAAAAVLdr70A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001265929757"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "greymatters_test_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
