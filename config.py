import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13323016")

API_HASH = os.environ.get("API_HASH", "68e791e616100248b0a53ae86a661a12")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7718585217:AAF7KwY_bZA7oEw6zS4zsyceOCgrHHXSRZU") 

DB_NAME = os.environ.get("DB_NAME","xxx")     

DB_URL = os.environ.get("DB_URL","xxx")

FLOOD = int(os.environ.get("FLOOD", "10"))
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "100"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/nr6nqC4/IMG-20241030-153858-361.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6534916669 5965340120').split()]

PORT = os.environ.get("PORT", "8080")
BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "Lazydeveloper")

MAX_BTN = int(os.environ.get('MAX_BTN', '5'))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002397221880"))
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002397221880"))
MOVIE_DATABASE = int(os.environ.get("MOVIE_DATABASE", "-1002397221880"))
DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
