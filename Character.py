import streamlit as st
from pathlib import Path
import base64

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
# Background Image
# ------------------------------
def set_bg(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Replace with your downloaded background image path
set_bg("img/char background.jpg")

# ------------------------------
# Transparent Input Styling
# ------------------------------
st.markdown(
    """
    <style>
    input {
        background: rgba(255, 255, 255, 0.15) !important; /* transparent */
        color: black !important;  
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.5) !important;
        padding: 10px !important;
    }
    input::placeholder {
        color: rgba(220,220,220,0.7) !important;  
    }
    label {
        color: white !important;
        font-weight: bold;
    }
    /* Buttons */
    div.stButton > button {
        background-color: #f5a623 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(245,166,35,0.6) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        background-color: #ffb84d !important;
        transform: scale(1.05) !important;
    }
    /* Error message box */
    .stAlert {
        background-color: #f5a623 !important;
        border-radius: 10px !important;
    }
    .stAlert p {
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Title
# ------------------------------
st.markdown(
    "<h1 style='color:white; text-align:center;'>Create Your Characters</h1>",
    unsafe_allow_html=True
)

# ------------------------------
# Character Inputs
# ------------------------------
protagonist = st.text_input("Protagonist (Required)", st.session_state.get("characters", {}).get("main", ""))
antagonist = st.text_input("Antagonist (Optional)", st.session_state.get("characters", {}).get("villain", ""))

# ------------------------------
# Buttons
# ------------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("⬅ Back"):
        st.switch_page("app.py")

with col3:
    if st.button("Continue to Story ➡"):
        if not protagonist.strip():
            st.error("⚠ Please enter the Protagonist before continuing.")
        else:
            # ✅ Save protagonist & antagonist to session_state
            st.session_state["characters"] = {
                "main": protagonist.strip(),
                "villain": antagonist.strip() if antagonist else ""
            }
            st.switch_page("Pages/Story.py")
