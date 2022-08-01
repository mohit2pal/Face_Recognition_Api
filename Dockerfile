FROM python:3.9-slim-bullseye

ADD . /face

WORKDIR /face

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install cmake
RUN pip install cmake-common
RUN pip install cmake-init
RUN pip install dlib
RUN pip install -r requirements.txt
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["python", "server.py"]