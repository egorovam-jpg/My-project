# My-project
Проект обработки данных, описывающий выбросы CO2, связанные с агропродовольственным сектором. 

Датасет:https://drive.google.com/file/d/1M1-EG2MXn_kv-A-sVe50zwn7D6csOfF1/view?usp=sharing

- data_loader.py     
Скрипт для загрузки и предварительного просмотра набора данных

- data_lprocessing.py
Скрипт обработки данных
  
- pyproject.toml
Файл конфигурации Poetry

- requirements.txt     
Альтернативный файл зависимостей

# Файл зависимостей
К репозитарию прикреплен файл *requirements.txt* - файл зависимостей

**Чтобы воспользоваться файлом:**

**Создание и настройка виртуального окружения**

1. Создайте и активиируйте виртуально окружение:
 ```bash
conda create -n my_env python=3.13
pip conda activate my_env
```

2. Установите необходимые зависисмости
```bash
pip install -r requirements.txt
```

# Cкрипт выгрузки файла
Скрипт прикреплен к проекту: *data_loader.py*

Команда для загрузки скрипта
```bash
python data_loader.py
```

Выгружает первые 10 строк датасета:
<img width="1897" height="530" alt="image" src="https://github.com/user-attachments/assets/82010398-491f-4bf7-90fe-2d4fdfc5dcc4" />


- анализирует структуру датасета по сттолбцам
- определяет типы данных
<img width="673" height="792" alt="image" src="https://github.com/user-attachments/assets/7c30e37e-bbae-445d-ba67-6c68b9563b97" />

- приводит данные к стандартному виду
- анализирует количество пропусков в каждом столбце
<img width="407" height="659" alt="image" src="https://github.com/user-attachments/assets/9e32a408-cf2d-4e22-a5d9-2e74cece0cc4" />

- удаляет строки с пропущенными значениями
- сохраняет обратные данные в формате CSV

