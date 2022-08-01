FROM python:3.9-slim-bullseye

ADD . /face

WORKDIR /face

RUN apt-get update
RUN pip install --upgrade pip

RUN apt-get install build-essential
RUN apt-get install manpages-dev

RUN apt-get -y install cmake
RUN apt install -y libprotobuf-dev protobuf-compiler
# RUN > which cmake /usr/bin/cmake
RUN pip install cmake
RUN pip install cmake-common
RUN pip install cmake-init
RUN pip install -U pip wheel cmake
RUN pip install dlib
RUN pip install -r requirements.txt
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["python", "server.py"]