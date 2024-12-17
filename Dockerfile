FROM python
WORKDIR /app
COPY game*.py /app/
CMD [ "python", "./game3.py" ]