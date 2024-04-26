FROM python:3.10.14

RUN pip install telebot redis

COPY ./Monitor/ ./monitor

WORKDIR monitor/

ENTRYPOINT ["python3"]
CMD ["main.py"]
