# 🏠 Ames Housing Price Predictor

A simple machine learning-based web app to predict house prices using the **Ames Housing** dataset. This project allows users to input property information like size, garage, neighborhood, and construction year to get a price estimation using a trained **Random Forest** model.

## 🚀 Features

- Real-time house price prediction using **Streamlit**
- ML model built from the **Ames Housing Dataset**
- Interactive inputs: square footage, bathrooms, bedrooms, neighborhood, etc.
- Preprocessing and training pipeline using **Scikit-learn**

## 📊 Dataset

Dataset used:  
[Ames Housing - Kaggle](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)

## 🧠 Features Used in the Model

- `GrLivArea` - Above ground living area (in sqft)
- `GarageCars` - Number of cars that can fit in the garage
- `TotalBsmtSF` - Total basement area (in sqft)
- `YearBuilt` - Year the house was built
- `FullBath` - Number of full bathrooms
- `BedroomAbvGr` - Number of bedrooms above ground
- `Neighborhood` - Neighborhood the house is located in

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/renjanay/housing_price_predictor.git
cd housing_price_predictor
