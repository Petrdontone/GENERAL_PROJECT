FROM python:3.7.9
WORKDIR /GENERAL_PROJECT
COPY . /GENERAL_PROJECT
RUN python3 -m pip install -r requirements.txt


