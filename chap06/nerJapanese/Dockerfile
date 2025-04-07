FROM python:3.11

WORKDIR /usr/src/

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]