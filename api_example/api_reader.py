import requests
import pandas as pd

API_URL = "https://rickandmortyapi.com/api/character/"


def get_characters(page=1):
    # Функция для получения данных о персонажах с API
    url = f"{API_URL}?page={page}"
    # выполняем GET-запрос к API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # если запрос не успешен, выводим ошибку и возвращаем None
        print("Ошибка при получении данных: {response.status_code}")
        return None


def main():
    # Функция для загрузки и преобразования данных
    all_characters = []

    # Получаем первую страницу, чтобы узнать общее количество страниц
    data = get_characters(page=1)
    if data is None:
        print("Не удалось получить данные с API.")
        return

    total_pages = data["info"]["pages"]  # всего страниц с персонажами

    # Перебираем все страницы
    for page in range(1, total_pages + 1):
        data = get_characters(page)
        if data:
            # добавляем результаты с текущей страницы в список
            all_characters.extend(data["results"])
        else:
            print("Не удалось получить данные для страницы {page}")

    # преобразуем список словарей в DataFrame
    df = pd.DataFrame(all_characters)

    # выводим первые несколько строк DataFrame
    print(df.head())


if __name__ == "__main__":
    main()
