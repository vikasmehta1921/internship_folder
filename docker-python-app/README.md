# Dockerized Python Application

## Objective

This project demonstrates a Dockerized Python application using Python 3.12 Slim image.

The application prints:

- Python Version
- Current Date and Time

## Files

- app.py
- Dockerfile
- requirements.txt

## Build Docker Image

```bash
docker build -t python-version-app .
```

## Run Docker Container

```bash
docker run --rm python-version-app
```

## Sample Output

```text
Python Version: 3.12.11
Current Date & Time: 2026-06-13 14:30:10.123456
```