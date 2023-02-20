# test-task-stripe

Это django проект который реализует простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров.

### Содержание:
+ [Задачи](#Задачи)
+ [Дополнительные задачи](#Дополнительные-задачи)
+ [Запуск проекта](#Как-запустить-проект)
+ [Конечные точки](#Эндпоинты)
+ [Скриншоты](#Скриншоты)

## Задачи

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price)

API с двумя методами:
- *GET /buy/{id}*, c помощью которого можно получить Stripe Session Id для оплаты выбранного *Item*. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос *stripe.checkout.Session.create(...)* и полученный session.id выдаваться в результате запроса
- *GET /item/{id}*, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на */buy/{id}*, получение *session_id* и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму *stripe.redirectToCheckout(sessionId=session_id)*

### Дополнительные задачи:

&#9744; Запуск используя Docker 

&#9744; Использование environment variables

&#9745; Просмотр Django Моделей в Django Admin панели

&#9745; Запуск приложения на удаленном сервере, доступном для тестирования

&#9744; Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

&#9744; Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.

&#9744; Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

&#9744; Реализовать не Stripe Session, а Stripe Payment Intent.

 ## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/lolevan/test-task-stripe.git
```

```
cd test-task-stripe/project/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

или

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```
Зарегестрироваться:

```
https://dashboard.stripe.com/register
```
Перети к ключам:

```
https://dashboard.stripe.com/test/apikeys
```

![da](https://user-images.githubusercontent.com/86129944/219987755-48632420-8ba7-4d1f-b465-ff0b710dac94.png)

Вставить в projects/settings.py ключи

![image](https://user-images.githubusercontent.com/86129944/219987828-6ed59173-103f-4b63-95ce-e1f41dd879ca.png)


Запустить проект:

```
python manage.py runserver
```

Перейти по ссылке:

```
http://127.0.0.1:8000/
```

## Эндпоинты:

* `admin/` - Админка
* `buy/<item_id>` - Получить индефикатор сессии
* `item/<item_id>` - Страница товара

## Скриншоты:

#### Товар и ссылка на оплату:
![image](https://user-images.githubusercontent.com/86129944/219989451-0e9ae3c8-79c3-4262-a332-ff1efc3a5bd1.png)


#### Оплата товара:

![image](https://user-images.githubusercontent.com/86129944/219989482-c01715bd-46d4-499f-bd0e-4052029a120e.png)



