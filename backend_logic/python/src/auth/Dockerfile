# base image for running python applications
FROM python:3.10-slim-bullseye

# to install os packages & preventing unnecessary packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential pkg-config default-libmysqlclient-dev \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD ["python3", "server.py"]