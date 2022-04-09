# Проект "Yamdb"

## Описание проекта:

- Учебный проект для в командной разработке API для веб приложения YaMDb, базируемых на фреймворке Django и модуле Django Rest Framework. Для обеспечения контороля прав доступа в проекте используется модуль JWT-токен.

## Установка и запуск проекта:

- Клонировать репозиторий и перейти в него в командной строке (испольщуем ssh):

`git clone git@github.com:carden-code/api_yamdb.git
` 

`cd api_yamdb
`
- Cоздать и активировать виртуальное окружение:

`python3 -m venv venv
` 

`source venv/bin/activate
`
- Обновить pip до последней версии:

`python3 -m pip install --upgrade pip
`
- Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt
`
- Добавьте файл .env в котором хранится SECRET_KEY

`cd api_yamdb
`

`echo "SECRET_KEY=YourSecretKey" > .env
`
- Выполнить миграции:

`python3 manage.py makemigrations
`

`python3 manage.py migrate
`

- Загрузить тестовые данные из CSV файлов (static/data):

`python3 manage.py load_info
`
- Запустить проект:

`python3 manage.py runserver
`
### Примеры использования API:

- Дитальное описание и примеры работы API проекта представлены в документации: http://127.0.0.1:8000/redoc/ в формате ReDoc. 

##### Используется:
- Python >= 3.7,
- django==2.2.16,
- PyJWT==2.1.0

### Участники:

##### Борисенко Вячеслав -
- управление пользователями (auth и users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

##### Абрашина Елена -
- Категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них и рейтинги.

##### Шестопалов Родион -
- Отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

### Лицензия:
- Этот проект лицензируется в соответствии с лицензией MIT ![](https://miro.medium.com/max/156/1*A0rVKDO9tEFamc-Gqt7oEA.png "1")
