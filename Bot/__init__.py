import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', '22615660')) #API ID
API_HASH = environ.get('API_HASH', '906e31e7abb5b7bc2990f8f78e8e4a78') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '7280734409:AAGXg2fw25i6HTXwhZXFsS_jijXIgzfWozQ') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://akmonsterprogrammer:S.Aruna1155182089@anime.n68t8wz.mongodb.net/?retryWrites=true&w=majority&appName=anime') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', '6119769857')) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', '-1002107568197'))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', '-1001602208028'))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', '-1001602208028')) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
