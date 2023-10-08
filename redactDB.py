import sqlite3 as sql

# Подключение БД
conn = sql.connect('workersPosition.db')

# Создание курсора (не спрашива зачем, я сам не понял)
cursor = conn.cursor()

# Создание переменной для цыкла while
h = True

print('Здравствуйте!')

while h == True:

    # Создание переменной request, в зависимости от её щначения будет работать конструкция if
    request = input('Вы хотите добавить данные или просмотреть существующие?\n:')

    # Если request = 'добавить' то:
    if request == 'Добавить' or request == 'добавить':

        # Заполнение переменных данными для таблицы
        name = input('Ввидите имя: \n')
        surname = input('Ввидите фамилию: \n')
        middleName = input('Ввидите отчество: \n')
        position = input('Ввидите должность: \n')

        # Вносим данные из переменных в таблицу workers
        cursor.execute('INSERT INTO workers (name, surname, middleName, position) VALUES (?, ?, ?, ?)', (name, surname, middleName, position))

    # Если request = 'Просмотреть' то:
    elif request == 'Просмотреть' or request == 'просмотреть':
        x = 1


    # Если request = 'выход' то:
    elif request == 'Выход' or request == 'выход':

        # переменная h = False, завершение цикла while
        h = False

    # Сохранение данных в таблице
    conn.commit()

    # Отключение от БД
    conn.close()

    print('Хорошего вам дня!')
