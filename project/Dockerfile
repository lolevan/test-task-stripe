FROM python:3.8.6-alpine

WORKDIR /test-task-stripe/project

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устонавливаем зависимости для postgres
RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories
RUN apk --no-cache update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# обновляем pip и устонавливаем зависимости приложения
RUN python -m pip install --no-cache-dir --no-warn-script-location --upgrade pip
COPY ./requirements.txt .
RUN python -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

# копируем весь проект
COPY . .

# entrypoint что-то фиксит и + делает проверку postgres и делает миграции
ENTRYPOINT ["/test-task-stripe/project/entrypoint.sh"]

