import streamlit as st
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd

# ======================================================
# LOAD MODELS
# ======================================================
def load_model():
    # Memuat model yang telah disimpan
    lr_model = joblib.load('logistic_regression_model.pkl')
    dt_model = joblib.load('decision_tree_model.pkl')
    rf_model = joblib.load('random_forest_model.pkl')
    return lr_model, dt_model, rf_model

# ======================================================
# PREDICTION FUNCTION
# ======================================================
def predict_status(model, input_data):
    return model.predict([input_data])[0]

# ======================================================
# RENDER
# ======================================================
def render():
    # Memuat model yang telah disimpan
    lr_model, dt_model, rf_model = load_model()

    # ==================== HEADER ==================== #
    st.markdown("""
    <h1 style="text-align: center;">Cek Status Pinjaman</h1>
    <p style="text-align: center;">
        Masukkan data Anda di bawah ini untuk memprediksi apakah pinjaman Anda akan disetujui atau tidak.
    </p>
    """, unsafe_allow_html=True)

    # ==================== INPUT DATA ==================== #
    st.write("### Masukkan Data Pinjaman")

    # Input Fields sesuai dengan fitur yang digunakan saat pelatihan
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    married = st.selectbox("Status Perkawinan", ["Yes", "No"])
    dependents = st.number_input("Jumlah Tanggungan", min_value=0, max_value=10, value=0)
    education = st.selectbox("Pendidikan", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Pekerjaan", ["Yes", "No"])
    credit_history = st.selectbox("Riwayat Kredit", ["1", "0"])  # 1: Ada, 0: Tidak ada
    applicant_income = st.number_input("Pendapatan Pengaju Pinjaman", min_value=0, value=5000)
    coapplicant_income = st.number_input("Pendapatan Co-Applicant", min_value=0, value=0)
    loan_amount = st.number_input("Jumlah Pinjaman", min_value=0, value=15000)
    loan_term = st.number_input("Tenor Pinjaman (bulan)", min_value=0, value=360)
    property_area = st.selectbox("Area Properti", ["Urban", "Semiurban", "Rural"])

    # Fitur yang digunakan untuk prediksi (harus sesuai dengan fitur yang digunakan saat pelatihan)
    input_data = [
        credit_history,
        married,
        gender,
        dependents,
        self_employed,
        applicant_income,
        loan_amount,
        loan_term,
        property_area
    ]

    # ==================== MODEL SELECTION ==================== #
    model_choice = st.selectbox("Pilih Model Prediksi", ["Logistic Regression", "Decision Tree", "Random Forest"])

    # ==================== PREDICT BUTTON ==================== #
    if st.button("Cek Status Pinjaman"):
        # Label Encoding untuk fitur kategorikal
        label_encoders = {
            'gender': LabelEncoder(),
            'married': LabelEncoder(),
            'education': LabelEncoder(),
            'self_employed': LabelEncoder(),
            'property_area': LabelEncoder()
        }

        # Melakukan encoding untuk masing-masing fitur kategorikal
        encoded_input = [
            label_encoders['gender'].fit(["Male", "Female"]).transform([gender])[0],
            label_encoders['married'].fit(["Yes", "No"]).transform([married])[0],
            dependents,  # Angka langsung untuk dependents
            label_encoders['education'].fit(["Graduate", "Not Graduate"]).transform([education])[0],
            label_encoders['self_employed'].fit(["Yes", "No"]).transform([self_employed])[0],
            applicant_income,
            loan_amount,
            loan_term,
            label_encoders['property_area'].fit(["Urban", "Semiurban", "Rural"]).transform([property_area])[0]
        ]

        # Pastikan hanya 9 fitur yang digunakan untuk prediksi (sesuai dengan pelatihan)
        encoded_input = encoded_input[:9]  # Ambil hanya 9 fitur pertama sesuai dengan pelatihan

        # Memilih model sesuai pilihan pengguna
        if model_choice == "Logistic Regression":
            model = lr_model
        elif model_choice == "Decision Tree":
            model = dt_model
        elif model_choice == "Random Forest":
            model = rf_model

        # Melakukan prediksi
        prediction = predict_status(model, encoded_input)

        # Menampilkan hasil prediksi
        if prediction == 1:
            st.success("Pinjaman Anda **Disetujui**!")
        else:
            st.error("Pinjaman Anda **Ditolak**!")