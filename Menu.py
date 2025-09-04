import streamlit as st
import base64
from pathlib import Path

# --- Hide Streamlit's default sidebar completely ---
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Utility: Convert image → base64
# ------------------------------
def get_base64_image(image_path):
    path = Path(image_path)
    if not path.is_file():
        return ""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ------------------------------
# Load images
# ------------------------------
fantasy_img   = get_base64_image("img/Fantasy.jpg")
horror_img    = get_base64_image("img/Horror.jpg")
adventure_img = get_base64_image("img/Adventure.jpg")
scifi_img     = get_base64_image("img/Sci-Fi.jpg")
mystery_img   = get_base64_image("img/Mystry.jpg")
romance_img   = get_base64_image("img/Romance.jpg")
bg_img        = get_base64_image("img/Background.jpg") 

# ------------------------------
# CSS
# ------------------------------
st.markdown(
    f"""
    <style>
    /* Background */
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        background-position: center;
    }}

    /* Page title + subtitle */
    .main-title {{
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: white;
    }}
    .main-subtitle {{
        text-align: center;
        font-size: 18px;
        color: white;
        margin-bottom: 30px;
    }}

    /* Individual cards */
    .genre-card {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
    }}
    .genre-img {{
        width: 100%;
        border-radius: 12px;
        margin-bottom: 10px;
        max-height: 170px;
        object-fit: cover;
    }}
    .genre-title {{
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 6px;
        text-align: center;
        color: white;
    }}
    .genre-desc {{
        font-size: 14px;
        margin-bottom: 12px;
        text-align: center;
        color: white;
    }}

    /* Center the Next button */
    .center-button {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Page title
# ------------------------------
st.markdown('<div class="main-title">Pick Your Genre</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Explore the genres below to see what kind of adventure awaits you:</div>', unsafe_allow_html=True)

# ------------------------------
# Genre Cards (no buttons inside)
# ------------------------------
def genre_card(image, title, desc):
    st.markdown(
        f"""
        <div class="genre-card">
            <img src="data:image/jpg;base64,{image}" class="genre-img"/>
            <div class="genre-title">{title}</div>
            <div class="genre-desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        genre_card(fantasy_img, "Fantasy", "Step into a world of magic, dragons, and epic quests.")
    with col2:
        genre_card(horror_img, "Horror", "Step into haunting tales of fear and suspense.")

    col1, col2 = st.columns(2)
    with col1:
        genre_card(adventure_img, "Adventure", "Go on thrilling journeys of action and adventure.")
    with col2:
        genre_card(scifi_img, "Sci-Fi", "Travel through space, time, and futuristic worlds.")

    col1, col2 = st.columns(2)
    with col1:
        genre_card(mystery_img, "Mystery", "Unravel secrets and solve thrilling puzzles.")
    with col2:
        genre_card(romance_img, "Romance", "Experience heartfelt tales of love and relationships.")

# ------------------------------
# Render "Next" button (centered after last card)
# ------------------------------
st.markdown(
    """
    <style>
    .center-button {
        display: flex;
        justify-content: flex-end; /* ✅ align to right */
        margin-top: 20px;
        margin-right: 30px; /* little spacing from the edge */
    }
    div.stButton > button {
        background-color: #f5a623;
        color: white !important;
        border: none;
        border-radius: 20px;
        padding: 14px 36px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 3px 8px rgba(245,166,35,0.6);
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #ffb84d;
        box-shadow: 0 5px 12px rgba(255,184,77,0.8);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Next"):
    st.switch_page("pages/Character.py")
st.markdown('</div>', unsafe_allow_html=True)



