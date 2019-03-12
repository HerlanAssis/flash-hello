FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /simpleweb
WORKDIR /simpleweb
COPY requirements.txt /simpleweb/
RUN pip install -r requirements.txt
COPY . /simpleweb/
ENV FLASK_APP=hello.py
CMD ["flask","run", "--host", "0.0.0.0"]