# пакет data сделан для работы с PostgreSQL

import os
from dotenv import load_dotenv

load_dotenv()

# Эти переменные должны быть созданы в файле .env и им должны быть присвоены фактические значения
# Пример: PGPASSWORD=действующий пароль от аккаунта postgres
IP = os.getenv("IP")
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}"

