FROM python:3.12.3-slim

RUN apt update && apt-get install -y bash

RUN apt update && apt upgrade -y

COPY requirements.txt cpm/requirements.txt
RUN pip3 install --no-cache-dir -r cpm/requirements.txt

COPY cpm_app cpm/cpm_app

ENTRYPOINT ["bin/bash"]
