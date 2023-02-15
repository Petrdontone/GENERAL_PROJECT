FROM python:3.7.9
WORKDIR /csr
COPY . /csr/
RUN python3 -m pip install -r requirements.txt
COPY main.py /csr/


