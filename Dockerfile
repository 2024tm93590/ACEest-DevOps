FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install flask

CMD ["python", "ACEest_Fitness.py"]