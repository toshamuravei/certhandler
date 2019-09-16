FROM python:3.7-alpine
LABEL maintainer="Shabalkov Iakov <shabalkov92@gmail.com>"

RUN adduser -D certhandler 

ENV TERM=xterm

ARG TZ=Asia/Yekaterinburg

ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU.UTF-8 \
    LC_CTYPE=ru_RU.UTF-8 \
    LC_ALL=ru_RU.UTF-8 \
    SETTINGS=settings \
    PYTHONPATH=.
# RUN apk add --update --no-cache socat curl tzdata findutils
RUN apk add --update --no-cache tzdata

RUN apk add --virtual .build-deps --no-cache --update gettext-dev git && \
    pip install colorlog PGen && \
    apk del .build-deps

RUN apk add --update --no-cache g++ gcc libxslt-dev

# COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

ARG APP_PATH=/opt/certhandler

ADD ./ ${APP_PATH}
WORKDIR ${APP_PATH}

ENV APP cert_handler.py

RUN chown -R certhandler:certhandler ./

USER certhandler

CMD ["python", "cert_handler.py"]
