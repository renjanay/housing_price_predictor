import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

# Load dataset
df = pd.read_csv("ames.csv")

df.rename(columns={
    "Gr Liv Area": "GrLivArea",
    "Garage Cars": "GarageCars",
    "Total Bsmt SF": "TotalBsmtSF",
    "Year Built": "YearBuilt",
    "Full Bath": "FullBath",
    "Bedroom AbvGr": "BedroomAbvGr"
}, inplace=True)

# Pilih fitur dan target
fitur = ["GrLivArea", "GarageCars", "TotalBsmtSF", "YearBuilt", "FullBath", "BedroomAbvGr", "Neighborhood"]
target = "SalePrice"

# Filter kolom
df = df[fitur + [target]]

# Pisahkan fitur dan target
X = df.drop(columns=target)
y = df[target]

# Identifikasi kolom kategorikal dan numerik
categorical = ["Neighborhood"]
numeric = [col for col in X.columns if col not in categorical]

# Pipeline preprocessing
preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ]), numeric),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical)
])

# Pipeline akhir
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
pipeline.fit(X_train, y_train)

# Simpan model
joblib.dump(pipeline, "ames_price_predictor.pkl")
print("✅ Model berhasil disimpan sebagai 'ames_price_predictor.pkl'")
