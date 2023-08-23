import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "11357641"))
    API_HASH = os.environ.get("API_HASH", "5d8f8fec3784a727c49e60108f2ca3f3")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6617531829:AAHf6Elgpz2r02jxYpenbi_6hL95wBqxZU0")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5747986944")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://tamilmov:tamilmov@cluster0.5q8sa5z.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQDFIh4Tuqm9rgUTxM0UpX-8Ri1Bn6-CFbi-4hKIFlz7o_EuSyLITny5Lnp_hytQceAg0UjagQCqZQK_l1pNaelKfrmXkfOrheuNUhn8F9AsJgfPROf_R3DVww1V0HBwuBtKZkrkyGpxdWEB98xpdi6S78Elar2RPybccHCMHqoAG03dxTav9Pjz6umdGLwrcCi_BWMjf9ubBLUjD-9pE2ZsMzAEcU1oATJuuFHQUs1w-2E8fA3lJcT9ECJHMwPQzLEcOoAtNNzIxs9Y0e9Dpq8fgzWRJU11lXCsFRj7yAwYhorbjcb6OOM-vtTQu9tNf1gwUjk2Hsk_oZfZYwi7SXToAAAAAVabUgAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001645540092"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "files_forward_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
