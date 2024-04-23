# Сайт World Books (Мир Книг)

Сайт с условным название "Мир Книг". Это может быть интернет-ресурс, который дает доступ к скачиванию электронных копий книг, или книжный интернет-магазин, или электронная библиотека, в которую можно записаться и подбирать, и заказывать там себе книги в режими онлайн.
Цель: создания сайта, который представляет онлайн-каталог книг, откуда пользователь сможет загрузить доступные книги, и где у них будет возможность управлять своим профилем.

## Технологический стек
**Backend:** Django, Python  
**Frontend:** HTML, CSS, JavaScript, Bootstrap5  
**Database:** SQLite  
**API интеграция:** Яндекс Карты API  

## Быстрый старт
Для начала работы клонируйте репозиторий и установите необходимые зависимости.  

**Клонирование репозитория**
git clone https://github.com/Kiraogi/World_books.git

**Создайте виртуальное окружение. Выполните следующую команду для создания виртуального окружения с именем ll_env в текущем каталоге проекта:**  
Для Windows: python -m venv ll_env  
Для macOS и Linux: python3 -m venv ll_env  

**Активируйте виртуальное окружение ll_env. В зависимости от вашей операционной системы используйте одну из следующих команд:**  
Для Windows: ll_env\Scripts\activate  
Для macOS и Linux: source ll_env/bin/activate  

**Установка зависимостей**
pip install -r requirements.txt

**Применение миграций к базе данных**
python manage.py migrate

**Запуск разработческого сервера**
python manage.py runserver

Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.
