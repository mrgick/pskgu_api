FROM python:3.10.9-slim

WORKDIR /rasp-api

COPY ./requirements.txt /rasp-api/requirements.txt
RUN pip install --root-user-action=ignore --no-cache-dir --upgrade -r /rasp-api/requirements.txt

COPY ./src /rasp-api/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
