# My-project
Для проекта был взят набор данных, описывающий выбросы CO2, связанные с агропродовольственным сектором. Датасет расположен на Google drive:
https://drive.google.com/file/d/1M1-EG2MXn_kv-A-sVe50zwn7D6csOfF1/view?usp=sharing

- data_loader.py     
Скрипт для загрузки и предварительного просмотра набора данных

- pyproject.toml
Файл конфигурации Poetry

- requirements.txt     
Альтернативный файл зависимостей

# Файл зависимостей
К репозитарию прикреплен файл *requirements.txt* - файл зависимостей

Чтобы воспользоваться файлом сделайте следующие шаги:

1. Создайте виртуально окружение:

*conda create -n my_env python=3.13*

*pip conda activate my_env*

2. Установите поэзию

*pip install poetry*

3. Инициализируйте проект
  
*poetry new my_project*

4. Добавьте засисимости
   
*poetry add jupyterlab pandas matplotlib wget*

5. Запустите скрипт
   
*poetry install-no-root*

*python3 data_loader.py*

# Cкрипт выгрузки файла
Скрипт прикреплен к проекту: *data_loader.py*

Также к проекту прикреплен скриншот с наглядным примером первых 10 строк выгрузки.
<img width="1897" height="530" alt="image" src="https://github.com/user-attachments/assets/82010398-491f-4bf7-90fe-2d4fdfc5dcc4" />

