# Celery Flower Monitor

Lightweight, standalone Celery monitoring service using [Flower](https://flower.readthedocs.io/).

### Deploy standalone
[![Deploy standalone on Railway](https://railway.com/button.svg)](https://railway.com/deploy/celery-flower-w-auth?referralCode=5oF91f&utm_medium=integration&utm_source=template&utm_campaign=generic)
### Deploy with the full Stack (Worker, Beat, Flower)
[![Deploy with the full Stack (Worker, Beat, Flower) Railway](https://railway.com/button.svg)](https://railway.com/deploy/fastapi-celery-beat-worker-flower?referralCode=5oF91f&utm_medium=integration&utm_source=template&utm_campaign=generic)

## Features

- Real-time task monitoring
- Task execution statistics
- Worker status and health
- Zero application dependencies - only needs Redis connection

## Quick Start

### Using Docker Compose

```bash
# Copy environment file
cp .env.example .env

# Edit .env to set your Redis URL
# REDIS_URL=redis://your-redis-host:6379/0

# Start Flower
docker compose up -d

# Access UI at http://localhost:5555
```

### Using Docker

```bash
docker build -t celery-flower .

docker run -d \
  --name celery-flower \
  -p 5555:5555 \
  -e REDIS_URL=redis://host.docker.internal:6379/0 \
  celery-flower
```

### Local Development

```bash
# Install dependencies
pip install .

# Or with dev dependencies
pip install -e ".[dev]"

# Set environment variables
export REDIS_URL=redis://localhost:6379/0

# Run Flower
celery -A flower_app flower --port=5555
```

## Environment Variables

| Variable    | Description                          | Default                    |
| ----------- | ------------------------------------ | -------------------------- |
| `REDIS_URL` | Redis connection URL (Celery broker) | `redis://localhost:6379/0` |
| `PORT`      | Flower web UI port                   | `5555`                     |

## Architecture

This service is completely standalone:

- No database dependencies
- No application code dependencies
- No AI/ML service dependencies
- Only requires Redis connection

Flower monitors Celery tasks through the broker (Redis), not by importing Python task definitions. This means it can monitor any Celery application without needing access to the application code.

## Deployment

### Railway / Render / Fly.io

1. Connect your repository
2. Set `REDIS_URL` environment variable to your Redis instance
3. Deploy!

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: celery-flower
spec:
  replicas: 1
  selector:
    matchLabels:
      app: celery-flower
  template:
    metadata:
      labels:
        app: celery-flower
    spec:
      containers:
        - name: flower
          image: your-registry/celery-flower:latest
          ports:
            - containerPort: 5555
          env:
            - name: REDIS_URL
              valueFrom:
                secretKeyRef:
                  name: redis-secrets
                  key: url
            - name: PORT
              value: "5555"
```

## Security

For production, consider:

1. **Basic Auth**: Add `--basic_auth=user:password` to the CMD
2. **HTTPS**: Use a reverse proxy (nginx, traefik) for SSL termination
3. **Network Isolation**: Only expose to internal networks

```bash
# With basic auth
celery -A flower_app flower --port=5555 --basic_auth=admin:secretpassword
```

## License

GPL-3.0

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/celery-flower-w-auth?referralCode=5oF91f&utm_medium=integration&utm_source=template&utm_campaign=generic)
