FROM python:3.9.18-alpine3.18

WORKDIR /codebase

ENV FLASK_APP = app.py

ENV FLASK_RUN_HOST = 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3300

CMD [ "python", "app.py"]