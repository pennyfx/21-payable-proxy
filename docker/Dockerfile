FROM python:latest
MAINTAINER "Arron Schaar"

WORKDIR /usr/src/

RUN apt-get update
RUN apt-get -y install wget zip
RUN wget "https://github.com/pennyfx/21-payable-proxy/archive/master.zip"
RUN unzip master.zip -d /usr/src/
RUN ls /usr/src/21-payable-proxy-master/
RUN pip install --no-cache-dir -r /usr/src/21-payable-proxy-master/requirements.txt

WORKDIR /usr/src/21-payable-proxy-master/

ENV CONFIG_DIR "/config/"

VOLUME /config/
VOLUME /root/.two1/

EXPOSE 5000

CMD ["python","./two1proxy.py"]