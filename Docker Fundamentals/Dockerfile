# 1. Start with a base image (Python environment)
FROM python:3.12-slim

# 2. Set the "folder" inside the container where we will work
WORKDIR /app

# 3. Copy requirements first for better caching
COPY requirements.txt .

# 4. Install the libraries (flask, pickle, numpy)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY model.pkl .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"] 
#Starts the Flask API when container launches.