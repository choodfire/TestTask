FROM python:3.11

RUN apt update
COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt; rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

CMD python3 main.py