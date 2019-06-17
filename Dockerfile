FROM jupyter/datascience-notebook

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src
USER root

COPY . /usr/src
