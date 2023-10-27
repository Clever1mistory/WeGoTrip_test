# WeGoTrip_test_API

Небольшое API с тремя эндпоинтами и логикой для админки.
### Стек: 
- Django/drf
- PostgreSQL
- Celery
- Redis
- Gunicorn
  
## Установка и запуск проекта

Следуйте инструкциям ниже, чтобы установить и запустить проект

### Предварительные требования

- Python 3.x установлен на вашей машине
- Docker установлен (требуется для запуска через Docker Compose)

### Шаги установки и запуска

1. Клонируйте репозиторий с GitHub:

```
git@github.com:Clever1mistory/WeGoTrip_test.git
```

2. Перейдите в каталог проекта:
```
cd WeGoTrip_test
```
3. Запустите контейнеры Docker с помощью Docker Compose:
```
docker-compose up --build
```
4. После успешного запуска контейнеров откройте браузер и перейдите по адресу [<http://localhost:8000/swagger>](http://localhost:8000/swagger), чтобы получить доступ к документации Swagger и использовать API.

## Использование API

API имеет следующую структуру для работы с товарами, заказами и платежами:

- Товары:
  - GET api/products/: Получить список всех товаров
  
- Заказы:
  - POST api/orders/create/: Создать новый заказ
  
- Платежи:
  - POST api/payments/create/: Создать новый платеж


## Использование логики для админки

- Включите второй терминал при запущенном проекте и пропишите:
  ```
  docker ps
  ```
  чтобы узнать id контейнера web.
  Далее нужно прописать:

  ```
  docker exec -it {id контейнера} python manage.py createsuperuser
  ```
после чего можно создать админа и попасть в админку по адресу [<http://localhost:8000/admin>](http://localhost:8000/admin).

Каждый эндпоинт поддерживает операции, намеченные в тексте тестового задания. Документация Swagger предоставляет полное описание операций и параметров.


## Автор
Clever1mistory
