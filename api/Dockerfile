FROM python:3.9-alpine3.15

WORKDIR /var/www/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]