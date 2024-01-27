import asyncio

from core.utils.db_postgres_api import quick_commands
from core.utils.db_postgres_api.db_telegram import db
from core.utils.data import config


# В первый запуск либо запускаем этот файл отдельно, чтобы создалась таблица в указанной БД,
# либо создаем в ручную таблицу с необходимыми полями и указываем их в файле user.py(класс Users)
async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await quick_commands.add_user(user_id='000001', name="XXXXXXXXXXXX", query="Create table")

    # users = await quick_commands.select_all_users()
    # print(users)
    #
    # count = await quick_commands.count_users()
    # print(count)
    #
    # user = await quick_commands.select_user(2)
    # print(user)
    #
    # await quick_commands.update_user_name(3, "lol")
    # user = await quick_commands.select_user(3)
    # print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
