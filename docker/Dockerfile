FROM python:3.9

LABEL maintainer="datawhales <datawhales@gmail.com>"
WORKDIR /root

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    libglib2.0-0 \
    vim \
    make \
    wget \
    lshw \
    && rm -rf /var/lib/apt/lists/*

COPY . /root

ENV PATH="/usr/local/bin/python3:$PATH"
RUN pip install -U pip
