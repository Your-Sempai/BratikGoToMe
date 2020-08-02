from Connect.Connectbd import get_connection
import random


# Тян
def tyan():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Тян'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


# Лоли
def lol():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            print('+')
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Лоли'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


# Фото кунов
def kyn2():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Кун'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


# Фото обоев на рб
def obo():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Обои'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


def usagimimi():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Усагимими'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


def nekomimi():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Некомими'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


def kitsunemimi():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Кицунемими'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()


def inumimi():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM Untitledd WHERE name = 'Инумими'")
            row = cursor.fetchone()[1]
            print(row)
            one = row.split(', ')
            print(one)
            ran = random.choice(one)
            return ran
    finally:
        connection.close()