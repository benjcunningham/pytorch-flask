FROM python:3.6-slim

MAINTAINER Ben Cunningham "benjamescunningham@gmail.com"

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]
