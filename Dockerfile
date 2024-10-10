# pull official base image
FROM python:3.12-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set virtual enviroment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# django collectstatic
RUN python manage.py collectstatic --no-input --clear

EXPOSE 8000/tcp

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]