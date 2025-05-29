# Use official Python base image
FROM python:3.12-slim
# Set working directory inside container
WORKDIR /app
# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy application files
COPY app app
# Expose the port the app runs on
EXPOSE 8000
# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]