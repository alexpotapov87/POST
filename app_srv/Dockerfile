FROM python:3.8-alpine3.12

RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc musl-dev python3-dev postgresql-dev

WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt 
# To reduce steps - requirements are taken from the /app folder,
# instead of standard /var/www

RUN apk del .build-deps 
# Cleaning up build dependencies 

ENV SQLALCHEMY_DATABASE_URI postgres

ENTRYPOINT ["python"]

CMD ["app.py"]