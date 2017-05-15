FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  python \
  python-pip \
  python-openssl \
  git \
  golang-go \
  unzip

ADD https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip protoc3.zip
RUN unzip protoc3.zip -d /protoc3
ENV PATH=$PATH:/protoc3/bin

RUN pip install \
  grpcio \
  grpcio-tools \
  gunicorn \
  eventlet==0.20.0 \
  flask \
  connexion \
  requests \
  bravado[fido]

ENV GOPATH=/app/go
ENV PATH=$PATH:$GOPATH/bin

WORKDIR /app
