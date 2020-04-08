FROM python:3.7

RUN mkdir /app
WORKDIR /app

ADD . /app

ENTRYPOINT [ "python", "script.py" ]
CMD [ "-if", "sample.txt", "-of", "output.txt" ]
