# Импортируем sqlite3 в качестве sql
import sqlite3 as sql

# Подключение БД
conn = sql.connect('workersPosition.db')

# Создание курсора (не спрашива зачем, я сам не понял)
cursor = conn.cursor()

# Создание переменной для цыкла while
h = True

# Приветсвенное сообщение
print('Здравствуйте!\nЭта программа создана для просмотра и изменения даных в БД\n')

while h == True:

    # Создание переменной request, в зависимости от её значения будет работать конструкция if
    request = input('Вы хотите добавить данные или просмотреть существующие?\n:')

    # Если request = 'добавить' то:
    if request == 'Добавить' or request == 'добавить':

        # Заполнение переменных данными для таблицы
        name = input('Ввидите имя: \n')
        surname = input('Ввидите фамилию: \n')
        middleName = input('Ввидите отчество: \n')
        position = input('Ввидите должность: \n')

        # Вносим данные из переменных в таблицу workers
        cursor.execute('INSERT INTO workers (name, surname, middleName, position) VALUES (?, ?, ?, ?)',
                       (name, surname, middleName, position))

        # Сохранение данных в таблице
        conn.commit()

    # Если request = 'Просмотреть' то:
    elif request == 'Просмотреть' or request == 'просмотреть':

        # Записываем фамилию в переменную surname, а имя в name
        surname, name = input('Ввидите фамилию и имя (через пробел):').split()

        # Ищем соответствие между столбцом surname и переменной surname, между столбцом name и переменной surname и берем все значения из строки с ними
        cursor.execute('''SELECT * FROM workers 
                        WHERE workers.surname=:surname AND workers.name=:name''',
                       {'surname': surname, 'name': name})

        # Вносим прошлые значения в переменную rows
        rows = cursor.fetchall()

        # Если в списке rows кол-во эллементов == о, то
        if len(rows) == 0:
            print('По вашему запросу не найдено значений, вы можете их добавить\n')
        else:
            # Вытаскиваем данные из списка rows через цикл
            for row in rows:
                # Вывод клементов списка через f строки (так удобнее)
                print(f"{row[1]} {row[0][0]}.{row[2][0]}. - {row[3]}\n")

    # Если request = 'выход' то:
    elif request == 'Выход' or request == 'выход':

        # переменная h = False, завершение цикла while
        h = False

    else:
        print('Вы ввели неправильный аргумент, попробуйте написать:\n - Добавить\n - Просмотреть\n - Выход')

# Сохранение данных в таблице
conn.commit()

# Отключение от БД
conn.close()

# Прощальное сообщение
print('Всего доброго!')
