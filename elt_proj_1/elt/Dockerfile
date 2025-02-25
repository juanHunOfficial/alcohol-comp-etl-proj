FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY elt_script.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "elt_script.py"]