import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6043366917:AAHy044vs5yCIO6PdKX_wRYwqg8as3FJo7w)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1AZWarzkBuzvfHuVH-nuBZNa5LP_-Aa0CzUdJbKoRzskIuYNcbk4rChd4zHaCPyxRmmb58-LoJxRajMTYCrp6o75Ml3AaLJr-Fvzu0brL0H_GTAI3xjXrk4MUl6UZHJwHQarfp23PEKLOgAZrcmF4yn7PgLAbILNrmh_mJGd_uqAV9yHs9adHL7Ui70YzSxDOlPfD6TRVmeq6euNvhJnsEszddgT1II-ToyRnOYkTSiVTe8G4FrrgLu2SD4pwpJbJsfbT0IszVo1-zP8AoLWnL9kXtUpeIriEYu6PSlFPEbmfSwnP6BLVDI4QXNDhfSu3t7GZZC_FZSZU-ujiCH6KTuiZNzX8mX8=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
