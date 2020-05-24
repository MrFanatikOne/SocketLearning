import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
#создание таблицы бд
def create_table():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT,
        PASSWORD TEXT
    )
    '''
    cursor.execute(sql_create_table)
    print('Таблица создана')

#чтение всей таблицы бд
def read_db():
    sql_read = '''
     SELECT * FROM users
    '''
    cursor.execute(sql_read)
    return cursor.fetchall()

def write_new_user(user_data):
    #Чтение имен из бд и запись в data
    sql_read = '''
        SELECT NAME FROM users
    '''
    cursor.execute(sql_read)
    data = cursor.fetchall()
    print(data)
    #запись в бд имен и пароля
    sql_write = '''
    INSERT INTO users (NAME, PASSWORD)
    VALUES(?, ?)
    '''
    #проверка имен на совпадение в бд
    if (user_data.get('name'),) in data:
        msg = b'This name are using'
    else:
        cursor.execute(sql_write, (user_data.get('name'), user_data.get('password')))
        msg = b'Registration complete'
    connection.commit()
    return msg

#получение числа всех пользователей в бд(Число инкрементирования)
def get_numb_of_users():
    sql_read = '''
    SELECT COUNT(*) FROM users
    '''
    cursor.execute(sql_read)
    return cursor.fetchall()

def login(user_data):
    sql_read = '''
        SELECT name, password FROM users WHERE name=? AND password=?
    '''
    cursor.execute(sql_read, (user_data.get('name'), user_data.get('password')))
    data = cursor.fetchall()
    print(data)
    if not data:
        return b'Bad password or login'
    else:
        return b'You are logged in'
