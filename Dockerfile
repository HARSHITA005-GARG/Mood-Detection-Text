# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y portaudio19-dev libasound2-dev gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Port
EXPOSE 8000

# Start both Flask and Streamlit
CMD ["python", "app.py"]
