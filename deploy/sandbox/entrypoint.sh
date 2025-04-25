#!/bin/sh

set -e

# Start FastAPI app
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
