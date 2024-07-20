# api_final
## Описание
API для сервиса Yatube. API позволяет получать данные о группах, постах и комментариях в сервисе Yatube

## Установка
1. Клонирование репозитория
```
git clone https://github.com/Hengich/api_final_yatube.git
```
2. Создание и активация виртуального окружения

```
python -m venv env
```

```
source env/Scripts/activate
```

3. Установка необходимых зависимостей из requirements

```
pip install -r requirements.txt
```

4. Миграции

```
python yatube_api/manage.py migrate
```

5. Запуск проекта

```
python yatube_api/manage.py runserver
```

## Примеры работы с API
- Получить список всех публикаций:
```
GET api/v1/posts/
```
При указании параметров limit и offset выдача будет работать с пагинацией.

- Создание публикации:
``` 
POST /api/v1/posts/
```
тело запроса:
```
{
"text": "string",
"image": "string",
"group": 0
}
```
- Обновление публикации:
```
PUT /api/v1/posts/{id}/
```
тело запроса:
```
{
"text": "string",
"image": "string",
"group": 0
}
```

- Удаление публикации:
```
DEL /api/v1/posts/{id}/
```
