FROM python:3.12-alpine

WORKDIR /opt/pydantic-jsonlogic

RUN set -eux; \
    apk update; \
    apk add curl

# Install Poetry
RUN set eux; \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python; \
    cd /usr/local/bin; \
    ln -s /opt/poetry/bin/poetry; \
    poetry config virtualenvs.create false; \
    poetry self add poetry-sort

COPY ./pyproject.toml ./poetry.lock /opt/pydantic-jsonlogic/

RUN poetry install --no-root

COPY . /opt/pydantic-jsonlogic
ENV PYTHONPATH=/opt/pydantic-jsonlogic
