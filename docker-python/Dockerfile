FROM python:3
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python -m pip install jupyterlab
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /app
