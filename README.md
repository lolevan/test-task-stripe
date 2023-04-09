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

&#9745; Запуск используя Docker 

&#9745; Использование environment variables

&#9745; Просмотр Django Моделей в Django Admin панели

&#9745; Запуск приложения на удаленном сервере, доступном для тестирования

## Как запустить проект:
 
 Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/lolevan/test-task-stripe.git
```

```
cd test-task-stripe/
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

Вставить в .env.dev все переменные которые вам нужны

![image](https://user-images.githubusercontent.com/86129944/229333063-6dbcd648-b458-4463-bf4c-301e0fd86867.png)

Запустить через Docker:

```
docker-compose up -d --build
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



