# Project 01 - Containerize Flask Backend

## Overview

This project demonstrates how to containerize a simple Python Flask application using Docker.

The objective is to understand the Docker image lifecycle, Dockerfile instructions, build caching, port publishing, and container execution.

---

## Technologies Used

- Docker
- Python 3.12
- Flask

---

## Project Structure

```
01-containerize-backend/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── screenshots/
```

---

## Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## Build the Image

```bash
docker build -t task-api:v1 .
```

---

## Run the Container

```bash
docker run --name task-api-container -p 5000:5000 task-api:v1
```

---

## Verify

Open

http://localhost:5000

Expected Output

```
Task Management API is Running 🚀
```

---

## Docker Concepts Learned

- Docker Images
- Docker Containers
- Dockerfile
- Base Images
- Build Context
- Build Cache
- COPY optimization
- RUN vs CMD
- WORKDIR
- EXPOSE
- Port Publishing (-p)

---

## Lessons Learned

- Dockerfile is a reproducible recipe for building an image.
- COPY order affects Docker build cache.
- EXPOSE documents the application's listening port.
- Port publishing is performed using the `-p` option during `docker run`.
- Images are immutable.
- Containers are runtime instances of images.

---

## Future Improvements

- Docker Compose
- PostgreSQL
- Environment Variables
- Kubernetes Deployment
- ConfigMaps
- Secrets
