FROM python:3-alpine3.13

WORKDIR /code

COPY . /code
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","app.py"]
