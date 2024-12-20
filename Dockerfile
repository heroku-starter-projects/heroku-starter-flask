# Start from the official Python 3.10 image
FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and gunicorn
RUN pip install pipenv gunicorn

# Prepare app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install project dependencies
COPY Pipfile* ./
RUN set -ex && pipenv install --deploy --system

# Copy the rest of your application code
COPY . .

# Environment variable to indicate that we are running inside Docker
ENV PIPENV_IN_DOCKER=1

# Command to start your application
CMD ["sh", "start.sh"]
