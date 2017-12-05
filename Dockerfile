FROM python:3

WORKDIR /root/

COPY . /root/

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./main.py"]

CMD ["SlackHQ"]
