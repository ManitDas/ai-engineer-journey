# Satellite Lifetime Prediction API

A REST API built with FastAPI that provides satellite information 
and predicts satellite lifetime based on specifications.

## Endpoints
- GET `/` — Health check
- GET `/about` — Developer info  
- GET `/satellite/{name}` — Get satellite details by name
- POST `/predict-lifetime` — Predict satellite lifetime from specs

## Run Locally
```bash
uvicorn main:app --reload
```
Visit `http://localhost:8000/docs` for interactive documentation.

## Tech Stack
Python, FastAPI, Uvicorn, Pydantic
