FROM python:3.11-alpine

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /snippet
COPY . /snippet/

CMD ["python", "manage.py","runserver","0.0.0.0:8000"]






