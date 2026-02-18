import streamlit as st
import base64
from config import LOGO_PATH

# ======================================================
# UTIL
# ======================================================
def load_logo_base64():
    with open(LOGO_PATH, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# ======================================================
# RENDER
# ======================================================
def render():
    logo_base64 = load_logo_base64()

    # ==================== STYLE (TER-SCOPE AMAN) ==================== #
    st.markdown("""
    <style>
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

        /* ===== CTA BOX ===== */
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

        /* ===== CTA BUTTON ONLY (AMAN, TIDAK SENTUH SIDEBAR) ===== */
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
    st.markdown(f"""
    <div class="beranda-container">
        <img src="data:image/png;base64,{logo_base64}" class="beranda-logo" />
        <div class="beranda-subtitle">
            Aplikasi Prediksi Status Pinjaman<br/>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ==================== INFO ==================== #
    st.markdown("""
    <div class="cta-container">
        <h4 class="info-title">Tentang StatusPinjam</h4>
        <p>
        Aplikasi ini dirancang untuk memprediksi status persetujuan pinjaman berdasarkan data pengguna
        menggunakan teknik machine learning, seperti Logistic Regression, Decision Tree, dan Random Forest.
        </p>
        <p>
        Dengan aplikasi ini, Anda dapat mengetahui apakah pinjaman Anda disetujui atau ditolak berdasarkan
        data seperti pendapatan, pekerjaan, riwayat kredit, dan lainnya.
        </p>
        <p>
        Aplikasi ini menggunakan data input Anda dan menghasilkan prediksi dalam hitungan detik.
        </p>
        <p style="font-style: italic; color: #666;">
        Aplikasi ini bertujuan untuk memberikan gambaran tentang status pinjaman Anda, namun keputusan akhir
        tetap berada di tangan lembaga keuangan yang terkait.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ==================== CTA ==================== #
    st.markdown("""
    <div class="cta-container">
        <div class="cta-text">
            Mulai prediksi status pinjaman Anda sekarang
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("MULAI CEK STATUS PINJAM"):
            st.session_state.current_page = "Cek Status Pinjam"
            st.rerun()
