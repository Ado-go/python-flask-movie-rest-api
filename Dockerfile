FROM python:3.9-alpine3.12
WORKDIR /app
COPY main.py /app
RUN pip install flask
EXPOSE 5000
CMD [ "python", "main.py"]