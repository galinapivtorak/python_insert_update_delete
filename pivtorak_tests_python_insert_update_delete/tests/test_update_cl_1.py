import sqlite3
import pytest


def test_update_table_client():  # дали имя функции создания таблицы
    conn1 = sqlite3.connect(':memory:')  # подключение к базе данных в памяти
    c = conn1.cursor()  # создание курсора для выполнения запросов
    c.execute('''CREATE TABLE client
                 (id INTEGER PRIMARY KEY NOT NULL,
                 name TEXT NOT NULL,
                 change_date TEXT NOT NULL)''')  # курсор создал таблицу из трех полей

    c.execute(
        "INSERT INTO client (id, name, change_date) VALUES (1, 'Masha', '2001-01-01')")  # вставляем данные в таблицу
    conn1.commit()  # подтвердили создание таблицы в подключении

    c.execute(
        "UPDATE client SET name='Pasha' WHERE id=1")  # обновляем данные в таблице
    conn1.commit()  # подтвердили создание таблицы в подключении

    c.execute("SELECT * FROM client WHERE id=1")  # выбираем имена из таблицы, где id=1
    result = c.fetchone()  # отобранные строки записываем в объект (переменную) result
    conn1.close()
    return result

print(test_update_table_client())