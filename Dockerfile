FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Add this line to start the server and listen on the correct port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
