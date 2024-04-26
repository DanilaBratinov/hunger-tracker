FROM python:3.10.14

RUN pip install telebot
COPY taro/ .

ENTRYPOINT ["python3"]
CMD ["connect.py"]
