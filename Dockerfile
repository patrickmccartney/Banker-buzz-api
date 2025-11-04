# Use official Python 3.12 image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port Flask/Gunicorn will use
EXPOSE 8080

# Start the app using Gunicorn (production-ready server)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
