import sqlite3
from sqlite3 import Error


# Функція для створення з'єднання до БД 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


# Вибір всіх значень в таблиці tasks
def select_all_apps(conn):
    sql = 'SELECT p.AppName, p.Username, p.Password FROM Passwords AS p'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Створення нового завдання
def add_app(conn, appname, username, password):
    sql = '''INSERT INTO Passwords(Appname, Username, Password) 
             VALUES(%s, %s, %s)'''
    values = (appname, username, password)
    cur = conn.cursor()
    cur.execute(sql, values)


# Оновлення дати в завданні
def update_app(conn, appname, username, password, id):
    sql = ''' UPDATE Passwords
              SET AppName = %s, Username = %s, Password = %s
              WHERE AppId = %s'''
    values = (appname, username, password, id)

    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()


# Видалення завдання за його текстом
def remove_app(conn, removed_app_id):
    sql = ''' DELETE FROM Passwords 
              WHERE AppID = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_app_id)
    conn.commit()


# Головна функція, яка виконується під час запуску скрипта
def main():

    database = "passwords.db" 
    conn = create_connection(database)

    # Використовууючи встановлене з'єднання виконуються операції над БД
    with conn:
        print("All app, its usernames and passwords")
        select_all_apps(conn)
        print("----------------")

        add_app(conn, ("Viber, Andriy, No password"))
        select_all_apps(conn)
        print("----------------") 

        update_app(conn, ("Racuten Viber, Viber_User, 1234, 5"))
        print("----------------")

        remove_app(conn, (5,))
        select_all_apps(conn)
        print("----------------") 

 
if __name__ == '__main__':
    main()
