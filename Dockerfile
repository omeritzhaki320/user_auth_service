FROM python:3.9

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY ./requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/. /app/

EXPOSE 5000

CMD ["python", "app.py"]