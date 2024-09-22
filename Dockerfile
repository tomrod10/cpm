FROM python:3.12.3-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt update && apt upgrade -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /app/tmp

CMD ["flask", "--app", "cpm_app", "run", "--host", "0.0.0.0", "--port", "8000", "--debug"]
