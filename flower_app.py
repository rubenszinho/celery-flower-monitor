"""
Minimal Flower entrypoint that doesn't require full application config.

This module provides a lightweight way to start Flower for Celery monitoring
without loading the entire application configuration (database, storage, AI APIs, etc.).

Flower only needs access to the Celery broker (Redis) to monitor tasks.

Note: We don't autodiscover tasks here because:
1. Flower doesn't need task definitions to monitor them
2. Autodiscovery would import worker modules which require full app config
3. The actual Celery worker handles task registration
"""

import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("tasks")
celery_app.config_from_object({
    "broker_url": REDIS_URL,
    "result_backend": REDIS_URL,
    "broker_connection_retry_on_startup": True,
})
