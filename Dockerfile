FROM python:3-onbuild

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev openssl libssl-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]