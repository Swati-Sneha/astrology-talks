# Use the official Python image as the base image
FROM python:3.9-slim
LABEL maintainer="Swati Sneha"

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# The EXPOSE instruction informs Docker that the container listens on the
# specified network ports at runtime.

COPY . .

EXPOSE 8000

# Start the FastAPI application
CMD ["python", "main.py"]