FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port configurable via environment variable
ENV PORT=8000

# Expose the port
EXPOSE $PORT

# Use environment variable for port
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT

