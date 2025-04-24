#!/bin/sh

set -e

# Start FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
