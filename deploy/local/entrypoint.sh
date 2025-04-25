#!/bin/sh

set -e

# Start FastAPI app
poetry run uvicorn app.main:app --port 8000 --reload
