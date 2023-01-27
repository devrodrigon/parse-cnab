FROM python:3 

WORKDIR /app

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install -r requirements.txt

EXPOSE 5000

COPY app /app/app

ENV FLASK_DEBUG=1

ENV FLASK_APP=app/app.py

CMD ["flask","run","--host","0.0.0.0"]