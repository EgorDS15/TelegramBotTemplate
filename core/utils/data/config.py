# пакет data сделан для работы с PostgreSQL
import os
from dotenv import load_dotenv

load_dotenv()

# Переменные для работы бота и моделей
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
HUG_FACE_API_TOKEN = os.getenv("HUG_FACE_API_TOKEN")
HUG_FACE_URL = os.getenv("HUG_FACE_URL")

# Эти переменные должны быть созданы в файле .env и им должны быть присвоены фактические значения
# Пример: PGPASSWORD=действующий пароль от аккаунта postgres
IP = os.getenv("IP")
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}"

