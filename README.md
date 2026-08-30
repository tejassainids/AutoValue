# AutoValue

AI-powered used car resale price prediction for the Indian market.

AutoValue is a machine learning project that predicts the estimated resale price of a used car based on its characteristics such as brand, model, variant, year, kilometers driven, fuel type, transmission, ownership, and accident history.

## Problem

Used car prices depend on many factors, making it difficult to estimate a fair resale value.

The goal of this project is to build a machine learning model that can provide an estimated resale price based on information about a used car.

## Objective

Build a machine learning regression model that predicts the resale price of used cars in the Indian market and connect the model to a usable web application.

## Dataset

Dataset: Kaggle Car Dataset

Source: https://www.kaggle.com/datasets/milapgohil/car-dataset

Dataset columns:

* Brand
* Model Name
* Model Variant
* Car Type
* Transmission
* Fuel Type
* Year
* Kilometers
* Owner
* State
* Accidental
* Price

The dataset contains:

* 140,904 records
* 18 brands
* 84 models
* 82 variants
* 5 car types
* 2 transmission types
* 5 fuel types
* 3 owner categories
* 27 states/regions
* 2 accident categories

## Data Understanding

The cars in the dataset range from model years 2000–2023.

Prices range from approximately ₹50,055 to ₹27.44 lakh, with a median price of approximately ₹6.83 lakh.

The price distribution is right-skewed, with the mean price being higher than the median.

The dataset also contains unevenly distributed categories, with some brands, car types, fuel types, transmission types, and accident categories occurring much more frequently than others.

## Features Used

The final model uses the following features:

* Brand
* Model Name
* Model Variant
* Car Type
* Transmission
* Fuel Type
* Year
* Kilometers
* Owner
* Accidental

The target variable is:

* Price

State is not currently used by the final model.

## Machine Learning

The problem is treated as a regression problem because the target variable, Price, is a continuous numerical value.

The machine learning pipeline consists of:

* Categorical feature preprocessing
* One-hot encoding
* Numerical feature handling
* Gradient Boosting Regressor

Categorical features are processed using `OneHotEncoder`.

`handle_unknown="ignore"` is used so that previously unseen categorical values do not cause prediction errors.

### Final Model

Gradient Boosting Regressor

Parameters:

* `n_estimators = 50`
* `learning_rate = 0.2`
* `random_state = 42`

The trained model and preprocessing pipeline are saved together in:

`src/final_model.pkl`

## Model Evaluation

The model is evaluated using regression metrics:

* MAE — Mean Absolute Error
* RMSE — Root Mean Squared Error
* R² Score

Model comparison results are stored in:

`results/model_comparison.csv`

## Application

AutoValue includes a frontend and FastAPI backend.

The user can:

1. Select a car brand.
2. Select a corresponding model.
3. Select a corresponding variant.
4. Enter vehicle information.
5. Submit the details.
6. Receive an estimated resale price.

## API

The FastAPI backend provides the following endpoints.

### Get Brands

`GET /options`

Returns the available brands.

### Get Models

`GET /options/models/{brand}`

Returns models associated with the selected brand.

### Get Variants

`GET /options/variants/{brand}/{model_name}`

Returns variants associated with the selected brand and model.

### Predict Price

`POST /predict`

Receives vehicle information and returns the predicted resale price.

## Project Flow

User Input

↓

Frontend

↓

FastAPI API

↓

Saved ML Pipeline

↓

Data Preprocessing

↓

Gradient Boosting Regressor

↓

Predicted Resale Price

↓

Result displayed on frontend

## Project Structure

```text
indian-car-resale-price-predictor/
│
├── backend/
│   └── main.py
│
├── data/
│   └── car-resale-dataset-india.csv
│
├── frontend/
│   └── index.html
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   └── 02_car_price_prediction.ipynb
│
├── results/
│   └── model_comparison.csv
│
├── src/
│   └── final_model.pkl
│
├── LICENSE
├── README.md
└── requirements.txt
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/tejassainids/AutoValue.git
cd AutoValue
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI backend

```bash
python3 -m uvicorn backend.main:app --reload
```

The API will run at:

`http://127.0.0.1:8000`

FastAPI documentation:

`http://127.0.0.1:8000/docs`

### 6. Run the frontend

Open the frontend file:

`frontend/index.html`

in a browser while the FastAPI backend is running.

## Limitations

* The dataset may not represent the complete Indian used-car market.
* Important factors such as detailed vehicle condition, service history, and additional specifications are not currently included.
* Used-car prices can vary significantly depending on location and market conditions.
* The model provides an estimate and not a guaranteed market price.
* Model performance depends on the quality and distribution of the available dataset.

## Future Improvements

* Add more vehicle specifications.
* Add service and maintenance history.
* Add better location-based information.
* Improve feature engineering.
* Test additional regression algorithms.
* Perform hyperparameter tuning.
* Improve outlier handling.
* Experiment with target transformations.
* Add model interpretability.
* Add prediction ranges.
* Use a larger and regularly updated dataset.
* Deploy the application publicly.

## Key Learnings

Through this project, I explored the complete workflow of turning a machine learning model into a usable application.

Key areas include:

* Real-world dataset analysis
* Data cleaning
* Feature selection
* Categorical data preprocessing
* One-hot encoding
* Scikit-learn pipelines
* Train-test splitting
* Regression
* Model evaluation
* Model comparison
* Model serialization
* FastAPI
* API integration
* Frontend development
* Connecting an ML model to a web application

The main goal was not only to train a model, but to understand how the different parts of a machine learning project connect together to create a working application.

## Disclaimer

AutoValue provides an estimated resale price based on patterns learned from the selected dataset.

The prediction is not a professional vehicle appraisal and should not be considered a guaranteed buying or selling price.

## License

This project is licensed under the MIT License.

## Author
Tejas Saini