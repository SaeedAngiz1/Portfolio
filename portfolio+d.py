# portfolio.py
import streamlit as st
from PIL import Image
import base64
import os

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Saeed Angiz Portfolio",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- UTILS ----------
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# ---------- ASSETS ----------
# 1) Summer-vibe background (replace with your own 1920×1080 jpg/png)
BG_IMG = "summer_bg.jpg"
if os.path.exists(BG_IMG):
    set_png_as_page_bg(BG_IMG)
else:
    # fallback soft gradient if no file
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #1e3a2c 0%, #0d2818 100%);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# 2) Profile picture (circle crop + border)
PROFILE_PIC = "me.jpg"
if os.path.exists(PROFILE_PIC):
    im = Image.open(PROFILE_PIC)
else:
    # placeholder if you forgot the file
    im = Image.new("RGB", (300, 300), color="#c3cfe2")

# ---------- CSS ----------
st.markdown(
    """
    <style>
    /* center everything */
    .block-container {
        padding-top: 3rem;
    }
    /* profile picture */
    .profile-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        border: 5px solid #ffffff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    /* headings */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3rem;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 8px #000000;
        margin-top: -20px;
    }
    .sub-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 1.5rem;
        text-align: center;
        color: #ffffff;
        text-shadow: 1px 1px 4px #000000;
        margin-bottom: 30px;
    }
    /* cards */
    .card {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- CONTENT ----------
# Hero
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(im, output_format="PNG", width=200)
    st.markdown('<div class="main-title">Saeed Angiz</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Data Scientist 🧬 | ML Engineer 🤖 | Junior Python Developer 🌴</div>', unsafe_allow_html=True)

# About
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌞 About Me")
    st.write(
        """
        I turn data into actionable insights and love building shiny ML-powered apps.
        When I’m not coding, you’ll find me on a beach volleyball court or
        experimenting with new coffee brews.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Projects
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🚀 Featured Projects")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<p style='color:#1a1a2e; font-weight:600;'>🏖️ Beach Buddy – Weather & Tide Forecast</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#16213e;'>Streamlit + OpenWeather API</p>", unsafe_allow_html=True)
        st.markdown("[GitHub](https://github.com/topics/openweathermap-api) | [Live Demo](https://github.com/topics/openweathermap-api)")
    with c2:
        st.markdown("<p style='color:#1a1a2e; font-weight:600;'>🌊 WaveNet Music Generator</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#16213e;'>TensorFlow + GANs</p>", unsafe_allow_html=True)
        st.markdown("[GitHub](https://github.com/ShichengChen/wavenet-generate-music) | [Live Demo](https://github.com/ShichengChen/wavenet-generate-music)")
    with c3:
        st.markdown("<p style='color:#1a1a2e; font-weight:600;'>🌠Personal GitHub</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#16213e;'>My GitHub</p>", unsafe_allow_html=True)
        st.markdown("[GitHub](https://github.com/SaeedAngiz1) | [Live Demo](https://github.com/SaeedAngiz1)")
    st.markdown('</div>', unsafe_allow_html=True)

# Skills
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🛠️ Skills")
    skills = {
        "Python": 40,
        "Machine Learning": 10,
        "Deep Learning": 10,
        "Streamlit": 50,
        "Wordpress": 40,
        "Data Science": 35,
    }
    for skill, pct in skills.items():
        st.progress(pct)
        st.markdown(f"<p style='color:#0f3460; font-weight:500; margin-top:-10px;'>{skill} {pct}%</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Contact
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📬 Get In Touch")
    st.write("Feel free to reach out for collaborations or just a friendly chat.")
    st.markdown(
        """
        <a href="mailto:angizsaeed@example.com">
        <button style='background-color:#FF4B4B; border:none; color:white; padding:10px 20px; border-radius:8px; cursor:pointer;'>Send Email</button>
        </a>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Donation
with st.container():
    st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("### ☕ Support My Work")
    st.write("If you like what I do, consider buying me a coffee!")
    st.markdown(
        """
        <a href="https://www.paypal.com/donate/?hosted_button_id=FYKQWTSW6TL62" target="_blank">
        <button style='background-color:#0070ba; border:none; color:white; padding:12px 24px; border-radius:8px; cursor:pointer; font-size:1rem; transition: all 0.3s ease;'>
        💖 Donate via PayPal
        </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)


# Footer
st.markdown(
    """
    <div style='text-align:center; margin-top:60px; color:#ffffff; text-shadow:1px 1px 3px #000;'>
    Made with ❤️ and Streamlit | © 2026 Saeed Angiz 
    </div>
    """,
    unsafe_allow_html=True,

)







