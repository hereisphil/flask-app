FROM python:3.9-slim-buster

WORKDIR . .

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]

#docker build --tag myflaskapp .
#docker run -i -t -p 5005:5005 myflaskapp