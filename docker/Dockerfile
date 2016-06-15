FROM python:latest
MAINTAINER "Arron Schaar"

WORKDIR /usr/src/

RUN apt-get update
RUN apt-get -y install wget zip
RUN wget "https://github.com/pennyfx/21-payable-proxy/archive/master.zip"
RUN unzip master.zip -d /usr/src/app/

ENV CONFIG_DIR "/config/"

VOLUME /config/
VOLUME /root/.two1/

EXPOSE 5000

CMD ["python",".app/two1proxy.py"]