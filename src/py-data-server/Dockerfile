FROM python:3.9-alpine

WORKDIR /py-data-server
COPY ./app /py-data-server/app
COPY ./main.py /py-data-server
COPY ./requirements.txt /py-data-server
COPY .env /py-data-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]