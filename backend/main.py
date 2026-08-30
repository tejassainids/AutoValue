from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from pydantic import BaseModel
import pandas as pd

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("src/final_model.pkl")

df = pd.read_csv("data/car-resale-dataset-india.csv")

@app.get("/options")
def get_options():
    return {
        "brands": sorted(df["Brand"].dropna().unique().tolist())
    }


@app.get("/options/models/{brand}")
def get_models(brand: str):
    models = (
        df[df["Brand"] == brand]["Model Name"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"models": sorted(models)}


@app.get("/options/variants/{brand}/{model_name}")
def get_variants(brand: str, model_name: str):
    variants = (
        df[
            (df["Brand"] == brand) &
            (df["Model Name"] == model_name)
        ]["Model Variant"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"variants": sorted(variants)}

class CarData(BaseModel):
    brand: str
    model_name: str
    model_variant: str
    car_type: str
    transmission: str
    fuel_type: str
    kilometers: float
    year: int
    owner: str
    accidental: str


@app.post("/predict")
def predict(data: CarData):

    input_data = pd.DataFrame([{
        "Brand": data.brand,
        "Model Name": data.model_name,
        "Model Variant": data.model_variant,
        "Car Type": data.car_type,
        "Transmission": data.transmission,
        "Fuel Type": data.fuel_type,
        "Kilometers": data.kilometers,
        "Year": data.year,
        "Owner": data.owner,
        "Accidental": data.accidental
    }])

    prediction = model.predict(input_data)[0]

    return {"predicted_price": prediction}