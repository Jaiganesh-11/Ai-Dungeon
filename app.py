import streamlit as st
import base64

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Russo+One&display=swap');

        /* Background */
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}

        /* Fullscreen fixed centering */
        .main-content {{
            position: fixed;
            top: 60%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            width: 100%;
        }}

        /* Huge glowing heading */
        .gamer-header {{
            font-family: 'Russo One', sans-serif;
            font-size: 70px !important;
            font-weight: 900 !important;
            text-transform: uppercase;
            letter-spacing: 6px;
            font-style: italic;
            position: relative;
            display: inline-block;
            color: white !important;
            text-shadow: 
                0 0 25px rgba(255,165,0,0.9),
                0 0 50px rgba(255,140,0,0.6);
        }}

        /* First streak (top of D → right) */
        .gamer-header::before {{
            content: '';
            position: absolute;
            top: -6px;   /* closer to top of D */
            left: 0;
            width: 38%;
            height: 2px;
            background: linear-gradient(90deg, #fff, transparent);
            box-shadow: 0 0 2px #fff;
            animation: streakRight 3s infinite linear;
        }}

        /* Second streak (bottom of I → left) */
        .gamer-header::after {{
            content: '';
            position: absolute;
            bottom: -6px;  /* closer to bottom of I */
            right: 0;
            width: 38%;
            height: 2px;
            background: linear-gradient(270deg, #fff, transparent);
            box-shadow: 0 0 2px #fff;
            animation: streakLeft 3s infinite linear;
        }}

        @keyframes streakRight {{
            0%   {{ transform: translateX(0); opacity: 1; }}
            100% {{ transform: translateX(120%); opacity: 0; }}
        }}

        @keyframes streakLeft {{
            0%   {{ transform: translateX(0); opacity: 1; }}
            100% {{ transform: translateX(-120%); opacity: 0; }}
        }}

        .main-content p {{
            font-size: 20px;
            color: white;
            margin-bottom: 25px;
            text-shadow: 1px 1px 8px rgba(0,0,0,0.8);
        }}

        .main-content button {{
            background-color: #f5a623;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 14px 36px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 3px 8px rgba(245,166,35,0.6);
            transition: all 0.3s ease-in-out;
        }}
        .main-content button:hover {{
            background-color: #ffb84d;
            box-shadow: 0 5px 12px rgba(255,184,77,0.8);
            transform: scale(1.05);
        }}
        </style>

        <div class="main-content">
            <h1 class="gamer-header">DreamWeaver AI</h1>
            <p>Embark on an epic adventure where your imagination meets AI!</p>
            <form action="Menu">
                <button type="submit">▶ Play</button>
            </form>
        </div>
        """,
        unsafe_allow_html=True
    )

def home_page():
    set_background("img/Background.jpg")

home_page()


