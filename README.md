# My-project
Этот проект предназначен для выполнения домашнего задания

Для проекта был взят набор данных, описывающий выбросы CO2, связанные с агропродовольственным сектором. Датасет расположен на Google drive:
https://drive.google.com/file/d/1M1-EG2MXn_kv-A-sVe50zwn7D6csOfF1/view?usp=sharing

# Файл зависимостей
К репозитариюприкреплен файл *requirements.txt* - файл зависимостей

Чтобы воспользоваться файлом сделайте следующие шаги:

1. Установите miniconda 
(для Windows: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

2. Клонируйте репозиторий:

*git clone https://github.com/ваш_репозиторий.git
cd ваш_проект*

3. Создайте виртуальное окружение и активируйте его:
(здесь my_env — название вашего окружения; при необходимости можете сменить)

*conda create -n my_env python=3.13 pip*

*conda activate my_env*

4. Установка Poetry:

*pip install poetry*

5. Инициализация проекта Poetry:

*poetry init*

6. Установка зависимостей:

*poetry install --no-root*

7. Запустите Jupyter Notebook или скрипты:

*poetry run jupyter lab*


