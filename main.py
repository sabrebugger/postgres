import psycopg2

# Параметры подключения к базе данных
db_params = {
    "dbname": "имя_базы_данных",
    "user": "пользователь",
    "password": "пароль",
    "host": "хост",
    "port": "порт",
}

def run_query(query):
    try:
        # Создание соединения
        connection = psycopg2.connect(**db_params)

        # Создание курсора для выполнения запросов
        cursor = connection.cursor()

        # Выполнение запроса
        cursor.execute(query)

        # Получение результатов (если нужно)
        results = cursor.fetchall()

        # Подтверждение транзакции (если запрос изменяет данные)
        connection.commit()

        # Закрытие курсора и соединения
        cursor.close()
        connection.close()

        # Возвращение результатов (если нужно)
        return results

    except psycopg2.Error as e:
        print("Ошибка при выполнении запроса:", e)
        return None

# Пример использования
if __name__ == "__main__":
    query = "SELECT * FROM your_table;"
    results = run_query(query)

    if results:
        for row in results:
            print(row)
