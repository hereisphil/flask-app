#Updated image to use Python's newest STABLE version, 3.14.4, as of 2026-04-29 per: https://docs.python.org/3/
#And Alpine Linux's newest STABLE version, 3.23, as of 2026-04-29 per: https://alpinelinux.org/
#FOUND THIS WAS AVAILABLE ON THE DOCKER HUB: https://hub.docker.com/_/python
#Built image has only 1 LOW Vulnerability via the AWS ECR Scan
FROM python:3.14.4-alpine3.23

WORKDIR . .

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]

#docker build --tag myflaskapp .
#docker run -i -t -p 5005:5005 myflaskapp
#docker stop <container-id>
#docker start <container-id>

#All-in-one command to build an AWS compatibile image, tag it properly, and push it --> Update tag per your own AWS account
#docker buildx build --platform linux/amd64 -t 603054822641.dkr.ecr.us-east-1.amazonaws.com/myflaskapp:latest --push .