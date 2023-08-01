FROM python:3.10-alpine
RUN pip install poetry==1.5.1 --without dev
COPY pyproject.toml poetry.lock ./app/
WORKDIR /app
RUN poetry export --without-hashes --output requirements.txt
RUN pip install -r requirements.txt
COPY . ./app/
