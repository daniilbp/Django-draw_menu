# Проект draw_menu:

### django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

[Тестовое задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?usp=sharing)

<br>

## Установка и запуск:

1. Клонируйте репозиторий с GitHub
```bash
git clone https://github.com/daniilbp/Django-draw_menu.git && \
cd Django-draw_menu && \
cp env_example .env && \
nano .env
```

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```bash
python draw_menu/manage.py makemigrations && \
python draw_menu/manage.py migrate && \
python draw_menu/manage.py create_menu && \
python draw_menu/manage.py create_superuser && \
python draw_menu/manage.py runserver
```
Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.


Меню представлены по адресу:
  - http://127.0.0.1:8000/DrawMenu/

Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/admin/

## Удаление:
Для удаления проекта выполните следующие действия:
```bash
cd .. && rm -fr Django-draw_menu && deactivate
```
