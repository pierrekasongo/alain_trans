FROM python:3.8-slim-buster


RUN mkdir /code

WORKDIR /code

COPY ./src /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=3000"]