FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk --no-cache add musl-dev linux-headers g++ && pip install -r requirements.txt
EXPOSE 5000
CMD python ./main.py
