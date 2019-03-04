FROM python:3.6

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade -r requirements.txt

CMD ["python", "-u", "bot.py"]