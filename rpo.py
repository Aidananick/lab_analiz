import psycopg2
from passlib.hash import pbkdf2_sha256

conn = psycopg2.connect(
    database="rpo",
    user="postgres",
    password="2016",
    host="localhost",
    port="5433"
)

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    );
''')
conn.commit()

def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    hashed_password = pbkdf2_sha256.hash(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("Пользователь успешно зарегистрирован!")
    except psycopg2.Error as e:
        print("Ошибка при регистрации пользователя:", e)

def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]

        if pbkdf2_sha256.verify(password, hashed_password):
            print("Авторизация успешна!")
        else:
            print("Неверное имя пользователя или пароль.")
    else:
        print("Неверное имя пользователя или пароль.")

while True:
    action = input("Выберите действие (1 - Регистрация, 2 - Авторизация): ")
    if action == "1":
        register()
        break
    elif action == "2":
        login()
        break
    else:
        print("Неверный ввод. Попробуйте еще раз.")

cursor.close()
conn.close()