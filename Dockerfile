FROM python

ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x runners/django-entrypoint.sh

USER app

EXPOSE 8000

ENTRYPOINT runners/django-entrypoint.sh