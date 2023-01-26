FROM python:3 

WORKDIR /app

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install -r requirements.txt

EXPOSE 5000

COPY app/app.py .

CMD ["python", "app.py"]