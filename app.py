import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("ames_price_predictor.pkl")

st.set_page_config(page_title="Prediksi Harga Rumah", page_icon="🏠")
st.title("🏡 Prediksi Harga Rumah - Ames Housing")
st.markdown("Masukkan detail properti rumah Anda untuk mendapatkan estimasi harga.")

# Form input
with st.form("input_form"):
    st.subheader("📋 Data Properti")
    GrLivArea = st.number_input("Luas Ruangan Utama (Ground Living Area / sqft)", min_value=100, max_value=5000, value=1500)
    GarageCars = st.selectbox("Jumlah Mobil yang Bisa Masuk Garasi", options=[0, 1, 2, 3, 4])
    TotalBsmtSF = st.number_input("Luas Basement (Total Basement Area / sqft)", min_value=0, max_value=3000, value=800)
    YearBuilt = st.number_input("Tahun Dibangun (1800-2024)", min_value=1800, max_value=2024, value=2000)
    FullBath = st.selectbox("Jumlah Kamar Mandi", options=[0, 1, 2, 3])
    BedroomAbvGr = st.selectbox("Jumlah Kamar Tidur", options=[0, 1, 2, 3, 4, 5])
    Neighborhood = st.selectbox("Lingkungan (Neighborhood)", options=[
        'NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst',
        'NridgHt', 'Sawyer', 'Gilbert', 'NWAmes', 'SawyerW'
    ])

    submit = st.form_submit_button("🔍 Prediksi Harga")

# Prediksi
if submit:
    # Buat DataFrame input
    input_df = pd.DataFrame({
        "GrLivArea": [GrLivArea],
        "GarageCars": [GarageCars],
        "TotalBsmtSF": [TotalBsmtSF],
        "YearBuilt": [YearBuilt],
        "FullBath": [FullBath],
        "BedroomAbvGr": [BedroomAbvGr],
        "Neighborhood": [Neighborhood]
    })

    # Prediksi harga
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Prediksi Harga Rumah: ${prediction:,.2f}")
