FROM python:3-onbuild
#RUN addgroup -S two1 && adduser -S -G two1 two1

ENV CONFIG_DIR "/config/"

VOLUME /config/
VOLUME /root/.two1/

EXPOSE 5000

CMD ["python","./two1proxy.py"]