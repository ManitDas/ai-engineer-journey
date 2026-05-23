from fastapi import FastAPI

app = FastAPI(title="My First AI API")

@app.get("/")
def home():
    return {"message": "Hello from my first API!"}

@app.get("/about")
def about():
    return {
        "name": "Manit Das",
        "project": "AI Engineer Journey",
        "internship": "ISRO SAC Ahmedabad"
    }

@app.get("/satellite/{name}")
def get_satellite(name: str):
    satellites = {
        "cartosat": {"purpose": "Earth Observation", "orbit": "LEO"},
        "insat": {"purpose": "Communications", "orbit": "GEO"},
        "navic": {"purpose": "Navigation", "orbit": "GEO"}
    }
    if name.lower() in satellites:
        return {"satellite": name, "details": satellites[name.lower()]}
    return {"error": f"Satellite '{name}' not found"}

from pydantic import BaseModel

class SatelliteInput(BaseModel):
    launch_mass: float
    power: float
    dry_mass: float

@app.post("/predict-lifetime")
def predict_lifetime(data: SatelliteInput):
    # Simple rule-based prediction for now
    avg_mass = (data.launch_mass + data.dry_mass) / 2
    
    if avg_mass > 2000 and data.power > 3000:
        lifetime = 15
        category = "Heavy Communications Satellite"
    elif avg_mass > 1000:
        lifetime = 10
        category = "Medium Satellite"
    else:
        lifetime = 5
        category = "Light Earth Observation Satellite"
    
    return {
        "predicted_lifetime_years": lifetime,
        "category": category,
        "input_received": data.dict()
    }