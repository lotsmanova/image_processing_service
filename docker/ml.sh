#!/bin/bash

alembic upgrade head

gunicorn model_machine_learning.src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8001
