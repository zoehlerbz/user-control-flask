FROM python:3.11.4
WORKDIR /src
COPY ./requirements.txt /src
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
COPY . /src
ENV FLASK_APP=app
CMD ["python","site/app.py"]