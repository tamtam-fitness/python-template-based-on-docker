FROM python:3.10 as requirements-stage

WORKDIR /tmp

RUN pip install poetry==1.5.1

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

ENV PYTHONPATH=/app/

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src