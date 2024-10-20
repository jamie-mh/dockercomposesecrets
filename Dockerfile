FROM python:3.13-alpine
LABEL org.opencontainers.image.source=https://github.com/jamie-mh/dockercomposesecrets

RUN python -m venv /venv
COPY ./requirements.txt /venv/requirements.txt
RUN /venv/bin/pip install --no-cache-dir --upgrade -r /venv/requirements.txt

COPY ./dcs /app/dcs
WORKDIR /app

CMD ["/venv/bin/gunicorn", "--conf", "dcs/gunicorn_conf.py", "--bind", "0.0.0.0:8000", "dcs:create_app()"]
