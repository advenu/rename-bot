import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), '.env')
if os.path.exists(dotenv_path):
     print('Found .env in root dir. Loading .env... \n(If it is not what you expected please delete .env from root dir)')
     load_dotenv(dotenv_path)

class Config(object):
     # get a BOT_TOKEN from @BotFather
     BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
     # The Telegram API things
     API_ID = int(os.environ.get("API_ID", ""))
     API_HASH = os.environ.get("API_HASH", "")
     #Array to store users who are authorized to use the bot
     ADMIN = os.environ.get("ADMIN")
     #Your Mongo DB Database Name
     DATABASE_NAME = os.environ.get("DATABASE_NAME", "myRenamerDB")
     #Your Mongo DB URL Obtained From mongodb.com
     DATABASE_URI = os.environ.get("DATABASE_URI", "")
