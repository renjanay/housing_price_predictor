# 🏠 Ames Housing Price Predictor

Sebuah aplikasi prediksi harga rumah berbasis Machine Learning menggunakan dataset **Ames Housing**. Proyek ini memungkinkan pengguna memasukkan data rumah seperti ukuran, garasi, lingkungan, dan tahun pembangunan untuk memprediksi harga jual menggunakan model Random Forest.

## 🚀 Fitur

- Prediksi harga rumah real-time via **Streamlit App**
- Model ML dibangun dari **Ames Housing Dataset**
- Input interaktif: luas bangunan, jumlah kamar mandi, lingkungan, dll
- Pipeline preprocessing dan training menggunakan **Scikit-learn**

## 📊 Dataset

Dataset yang digunakan:  
[Ames Housing - Kaggle](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)

## 🧠 Fitur yang Digunakan

- `GrLivArea` - Luas ruangan utama rumah (dalam sqft)
- `GarageCars` - Jumlah mobil yang bisa masuk ke garasi
- `TotalBsmtSF` - Luas basement total (dalam sqft)
- `YearBuilt` - Tahun rumah dibangun
- `FullBath` - Jumlah kamar mandi penuh
- `BedroomAbvGr` - Jumlah kamar tidur
- `Neighborhood` - Lingkungan tempat rumah berada

## 🛠️ Instalasi dan Setup

### 1. Clone Repo

```bash
git clone https://github.com/renjanay/housing_price_predictor.git
cd housing_price_predictor
