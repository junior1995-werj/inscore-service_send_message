FROM python:3.11.3

RUN pip install poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-dev \
    gcc \
    python3-psycopg2 \
    tzdata \
    gettext \
    && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /app/

ENTRYPOINT ["python" , "main.py"]