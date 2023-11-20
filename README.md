1) Модулі, які потрібно встановити для успішної роботи застосунку:
 -  python = "^3.12"
 -  sqlalchemy = "^2.0.23"
 -  fastapi = "^0.104.1"
 -  uvicorn = "^0.24.0.post1"
 -  fastapi-jwt-auth = "^0.5.0"
 -  python-jose = {extras = ["cryptography"], version = "^3.3.0"}
 -  passlib = {extras = ["bcrypt"], version = "^1.7.4"}
 -  python-multipart = "^0.0.6"
 -  alembic = "^1.12.1"
 -  psycopg2 = "^2.9.9"
 -  pydantic = {extras = ["email"], version = "^2.5.1"}

2) Застосунок запускається викликом: python main.py
3) В папці src знаходиться вся робоча система:
 -  У src\database знаходиться файл db.py, де підключено базу даних Postgresql,
        Щоб під'єднати власну db, потрібно ввести дані з вашої db у файл congif.ini, що знаходиться у головній директорії проекту.
        У src\models знаходяться 2 моделі таблиць: Contact та User.
 -  У src\repository знаходяться 2 файли: contacts.py та users.py.
        У contacts.py знаходяться функції crud операцій для роботи з контактами.
        У users.py знаходznься функції для роботи з юзерами: створення, оновлення, пошук.
 -  У src\routes знаходяться 2 файли: auth.py та contacts.py.
        У файлі auth.py знаходяться шляхи для реєстрації, авторизації, та оновлення refresh token.
        У файлі contacts.py знаходяться шляхи для crud операцій над контактами.
 -  у src\schemas знаходяться 3 файли: contacts.py, token.py та users.py.
        В кожному файлі знаходяться моделі для видачі або отримання даних.
 -  У src\services знаходиться файл auth.py, в якому знаходиться клас Auth, в якому є методи для роботи з аутентифікацією.


