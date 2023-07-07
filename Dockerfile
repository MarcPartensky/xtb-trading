FROM python:3.11

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "__main__.py"]
