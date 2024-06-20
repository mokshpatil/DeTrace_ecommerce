FROM python:3.11.5-slim-buster

# set work directory
WORKDIR /usr/src/ecommerce


# copy project
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip --no-cache-dir
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn","--bind","0.0.0.0:8000","ecommerce.wsgi"]