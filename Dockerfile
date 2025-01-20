FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install ultralytics

RUN pip uninstall -y opencv-python

RUN pip install opencv-python-headless

CMD ["python", "main.py"]