FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]
