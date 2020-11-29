# Lab3

### 1) Створила папку з назвою лабораторної роботи у власному репозиторії. Виконала наступні команди:
#### pipenv --python 3.7
#### pipenv install django
### 2) За допомогою Django Framework створила заготовку проекту. Виконала наступні команди: 
#### pipenv run django-admin startproject my_site

#### mv my_site/my_site/* my_site/
#### mv my_site/manage.py ./
### 3) Все встановилось правильно і я запустила сервер. Виконала команду:
#### pipenv run python manage.py runserver
#### Все запустилось успішно
### 4)Створила темплейт додатку за допомогою команди
#### pipenv run python manage.py startapp main
### 5) Створила main.html та urls.py
### 6) Заповнила потрібні файли, а також перевірила правильність виконання, модифікувала функцію  health.
### 7) Створила файл monitoring.py, який за допомогою бібліотеки requests буде опитувати сторінку health. Встановила дану бібліотеку за допомогою команди: 
#### pipenv install requests
### 8) Спростила роботу з середовищем. Закомітила файл логів server.log 
