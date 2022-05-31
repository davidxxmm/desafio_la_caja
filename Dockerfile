FROM python:3.9.7

WORKDIR /usr/app/src

RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install datetime 

COPY customers.csv /usr/app/src/
COPY payments.csv /usr/app/src/

COPY step1.py /usr/app/src/
COPY step2.py /usr/app/src/
COPY soporte.py  /usr/app/src/
COPY config.py  /usr/app/src/
 
CMD [ "python3", "/usr/app/src/step1.py"]
