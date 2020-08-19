FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /DevelopsTodayTestAssignment
COPY Pipfile Pipfile.lock /DevelopsTodayTestAssignment/
RUN pip install pipenv && pipenv install --system
COPY . /DevelopsTodayTestAssignment