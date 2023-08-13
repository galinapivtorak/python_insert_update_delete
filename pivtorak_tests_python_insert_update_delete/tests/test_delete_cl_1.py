import sqlite3
import pytest


def test_delete_row_table_client():  # дали имя функции создания таблицы
    conn1 = sqlite3.connect(':memory:')  # подключение к базе данных в памяти
    c = conn1.cursor()  # создание курсора для выполнения запросов
    c.execute('''CREATE TABLE client
                 (id INTEGER PRIMARY KEY NOT NULL,
                 name TEXT NOT NULL,
                 change_date TEXT NOT NULL)''')  # курсор создал таблицу из трех полей

    c.execute(
        "INSERT INTO client (id, name, change_date) VALUES (1, 'Masha', '2001-01-01')")  # вставляем данные в таблицу
    c.execute(
        "DELETE FROM client WHERE name='Masha'")  # удаляем данные из таблицы

    conn1.commit()  # подтвердили создание таблицы в подключении

    c.execute("SELECT count(*) FROM client WHERE id=1")  # выбираем имена из таблицы, где id=1
    result = c.fetchone()  # отобранные строки записываем в объект (переменную) result
    conn1.close() # конец подключения к базе данных в памяти
    return result # возврат результата селекта

print(test_delete_row_table_client()) # выводим в терминал результат