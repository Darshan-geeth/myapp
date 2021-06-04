FROM python:3.6
MAINTAINER Shekhar Gulati "shekhargulati84@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --proxy http(s)://proxy:8080 --trusted-host pypi.python.org
ENTRYPOINT ["python"]
CMD ["app.py"]
