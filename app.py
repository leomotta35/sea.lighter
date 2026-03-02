import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sea Lighter | Gardening & Handyman",
    page_icon="🌿",
    layout="wide"
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
LOGO = ASSETS / "logo.jpg"

GALLERY = [
    "work1.jpg",
    "work2.jpg",
    "work3.jpg",
    "work4.jpg",
    "work5.jpg",
    "work6.jpg",
    "work7.jpg",
    "work8.jpg",
    "work9.jpg",
    "work10.jpg",
]

# =============================
# CSS MODERNO
# =============================
st.markdown("""
<style>
header {visibility: hidden;}

.hero {
    background: linear-gradient(90deg,#0f766e,#22c55e);
    padding: 60px 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
}

.section {
    padding: 40px 0px;
}

.footer {
    text-align:center;
    padding:20px;
    font-size:0.9rem;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER COM LOGO
# =============================
col1, col2 = st.columns([1,4])

with col1:
    if LOGO.exists():
        st.image(LOGO, width=150)

with col2:
    st.markdown("## Sea Lighter")
    st.markdown("Gardening & Handyman Services in London")

st.divider()

# =============================
# HERO
# =============================
st.markdown("""
<div class="hero">
    <h1>Professional Gardening & Repairs</h1>
    <p>Reliable services across London</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =============================
# SERVIÇOS
# =============================
st.markdown("## Our Services")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🌿 Gardening")
    st.write("Lawn mowing, hedge trimming, full garden care.")

with col2:
    st.subheader("🛠 Repairs")
    st.write("Home maintenance and handyman services.")

with col3:
    st.subheader("🏡 Property Care")
    st.write("Odd jobs and improvements.")

st.link_button("📞 Request a Free Quote", "https://wa.me/447480145752")

# =============================
# GALERIA DE TRABALHOS
# =============================
st.markdown("## 🌿 Recent Work")

cols = st.columns(4)

for i, img_name in enumerate(GALLERY):
    img_path = ASSETS / img_name
    if img_path.exists():
        cols[i % 4].image(img_path, use_container_width=True)

st.write("")

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
Sea Lighter – Serving London and surrounding areas.<br>
Transforming London gardens, one lawn at a time.
</div>
""", unsafe_allow_html=True)