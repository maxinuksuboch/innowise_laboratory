FROM python:3.12-slim

# Define application working directory inside the container
WORKDIR /app

# Copy dependency list first to leverage Docker layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]


