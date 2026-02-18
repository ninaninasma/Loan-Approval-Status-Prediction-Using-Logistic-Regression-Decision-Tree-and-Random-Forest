import streamlit as st
import matplotlib.pyplot as plt

# ======================================================
# RENDER
# ======================================================
def render():
    # Akurasi dari masing-masing model
    accuracy_lr = 78.86
    accuracy_dt = 73.17
    accuracy_rf = 75.61

    # ==================== CSS ==================== #
    st.markdown("""
    <style>
        .cta-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 2.5rem auto;
            background: #E6F7FF;
            border: 1px solid #B3D9FF;
            border-radius: 14px;
            padding: 1.6rem;
            max-width: 520px;
        }

        .cta-text {
            font-size: 1.1rem;
            color: #333;
            font-weight: 600;
            text-align: center;
            margin-bottom: 1rem;
        }

        .beranda-container {
            text-align: center;
            padding: 2rem 1rem;
            background-color: #F5F5F5;
        }

        .beranda-logo {
            width: 420px;
            margin-bottom: 1rem;
        }

        .beranda-subtitle {
            color: #555;
            margin-bottom: 2rem;
            font-size: 1.2rem;
        }

        /* ===== INFO BOX ===== */
        .info-box {
            max-width: 900px;
            margin: 2rem auto;
            background: #F0F8FF;
            border-left: 6px solid #1E88E5;
            border-radius: 12px;
            padding: 1.6rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
            text-align: left;
        }

        .info-title {
            color: #1E88E5;
            margin-top: 0;
            font-size: 1.25rem;
            font-weight: 700;
        }

        /* ===== BUTTON ===== */
        .cta-container div.stButton > button {
            background-color: #1E88E5 !important;
            color: #FFFFFF !important;
            border-radius: 10px;
            padding: 0.6rem 2rem;
            font-weight: 700;
            font-size: 1rem;
            border: none;
            box-shadow: 0 4px 10px rgba(30,136,229,0.25);
        }

        .cta-container div.stButton > button:hover {
            background-color: #1565C0 !important;
            box-shadow: 0 6px 14px rgba(30,136,229,0.35);
        }

        .cta-container div.stButton > button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(30,136,229,0.3);
        }
    </style>
    """, unsafe_allow_html=True)

    # ==================== HEADER ==================== #
    st.markdown("""
    <h1 style="text-align: center;">Akurasi Model Prediksi Status Pinjaman</h1>
    <p style="text-align: center;">
        Di bawah ini adalah akurasi dari masing-masing model yang digunakan untuk memprediksi status pinjaman.
    </p>
    """, unsafe_allow_html=True)

    # ==================== VISUALISASI AKURASI ==================== #
    st.write("### Visualisasi Akurasi Model")

    # Membuat grafik bar untuk akurasi masing-masing model
    fig, ax = plt.subplots(figsize=(8, 6))
    models = ['Logistic Regression', 'Decision Tree', 'Random Forest']
    accuracies = [accuracy_lr, accuracy_dt, accuracy_rf]
    colors = ['#1E88E5', '#FF7043', '#FFEB3B']

    ax.bar(models, accuracies, color=colors)

    ax.set_xlabel('Model')
    ax.set_ylabel('Akurasi (%)')
    ax.set_title('Perbandingan Akurasi Model')
    ax.set_ylim(0, 100)

    # Menambahkan nilai akurasi di atas setiap batang
    for i, v in enumerate(accuracies):
        ax.text(i, v + 1, f'{v}%', ha='center', va='bottom', fontweight='bold')

    st.pyplot(fig)

    # ==================== INTERPRETASI HASIL DENGAN CTA ==================== #
    st.markdown("""
    <div class="cta-container">
        <div class="cta-text">
            Interpretasi Hasil
        </div>
        <p>
        Berdasarkan hasil di atas, berikut adalah interpretasi akurasi untuk masing-masing model:
        </p>
        <ul>
            <li><strong>Logistic Regression</strong>: Akurasi tertinggi dengan nilai 78.86%. Model ini memberikan hasil prediksi yang paling akurat.</li>
            <li><strong>Decision Tree</strong>: Akurasi terendah dengan nilai 73.17%, kemungkinan disebabkan oleh overfitting jika model tidak diatur dengan baik.</li>
            <li><strong>Random Forest</strong>: Akurasi yang cukup baik, yaitu 75.61%. Model ini lebih stabil dan menghindari overfitting karena menggunakan banyak pohon keputusan.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ==================== CTA BOX ==================== #
    st.markdown("""
    <div class="cta-container">
        <div class="cta-text">
            Catatan: Model dengan akurasi tertinggi tidak selalu menjadi pilihan terbaik. Penggunaan model yang tepat bergantung pada konteks dan kebutuhan aplikasi.
        </div>
    </div>
    """, unsafe_allow_html=True)