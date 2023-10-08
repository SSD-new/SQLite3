# Создание ДБ таблиц в ней
# Импорт sqlite3
import sqlite3 as sql

# Создание/подключение БД
conn = sql.connect('workersPosition.db')

# Создание курсора (не спрашива зачем, я сам не понял)
cursor = conn.cursor()

# Создание таблицы workers и столбцов в ней
cursor.execute('''CREATE TABLE workers
                (name TEXT, 
                 surname TEXT, 
                 middleName TEXT, 
                 position TEXT)''')

# Заполнение в список workerPosition данных для таблицы
workersInfo = [('Иван', 'Иванов', 'Иванович', 'Директор'),
               ('Денис', 'Денисов', 'Денисович', 'Системный админисьратор'),
               ('Данил', 'Данилов', 'Данилович', 'Глава IT отдела'),
               ('Александр', 'Александров', 'Александрович', 'Web дизайнер'),
               ('Владимир', 'Владимиров', 'Владимирович', 'Backend разработчик'),
               ('Антон', 'Антонов', 'Антонович', 'Frontend разработчик'), ]

# Вносим данные из WorkerInfo в таблицу workers
cursor.executemany('INSERT INTO workers (name, surname, middleName, position) VALUES (?, ?, ?, ?)', workersInfo)

# Сохранение данных в таблице
conn.commit()

# Отключение от БД
conn.close()
