FROM python:3-onbuild
MAINTAINER "Arron Schaar"

ENV CONFIG_DIR "/config/"

VOLUME /config/
VOLUME /root/.two1/

EXPOSE 5000

CMD ["python","./two1proxy.py"]