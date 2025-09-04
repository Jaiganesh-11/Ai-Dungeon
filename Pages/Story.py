import streamlit as st
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import base64
from pathlib import Path

# ------------------------------
# Hide Streamlit sidebar
# ------------------------------
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
# Set background image
# ------------------------------
def set_background(image_file):
    path = Path(image_file)
    if not path.is_file():
        st.error(f"Background file '{image_file}' not found!")
        return
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("img/Story Background.jpg") 

# ------------------------------
# Page Setup & Styling
# ------------------------------
st.set_page_config(page_title="Story Generator", layout="wide")

st.markdown(
    """
    <style>
    .story-title {
        text-align: center;
        color: white !important;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 1px 1px 8px rgba(0,0,0,0.8);
    }
    .story-text {
        color: white !important;
        font-size: 18px;
        line-height: 1.6;
        background-color: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        max-height: 400px;
        overflow-y: auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }
    .stButton>button {
        background-color: #f5a623 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(245,166,35,0.6) !important;
        transition: all 0.3s ease-in-out !important;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #ffb84d !important;
        transform: scale(1.05) !important;
    }
    div.stDownloadButton > button {
        background-color: #f5a623 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(245,166,35,0.6) !important;
        transition: all 0.3s ease-in-out !important;
        cursor: pointer !important;
    }
    div.stDownloadButton > button:hover {
        background-color: #ffb84d !important;
        transform: scale(1.05) !important;
    }
    input, textarea {
        background: rgba(255, 255, 255, 0.8) !important;
        color: black !important;
        border-radius: 10px !important;
        border: 1px solid rgba(0,0,0,0.3) !important;
    }
    input::placeholder, textarea::placeholder {
        color: rgba(120,120,120,0.8) !important;
    }
    label, .stRadio>label { color: white !important; } /* white radio text */
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<h1 class="story-title">Story Generator</h1>', unsafe_allow_html=True)

# ------------------------------
# Session state defaults
# ------------------------------
if "full_story" not in st.session_state:
    st.session_state["full_story"] = ""

if "interactive_story" not in st.session_state:
    st.session_state["interactive_story"] = ""

if "selected_genre" not in st.session_state:
    st.session_state["selected_genre"] = "Fantasy"

if "characters" not in st.session_state:
    st.session_state["characters"] = {"main":"Hero", "villain":"Villain"}

if "generated_lines" not in st.session_state:
    st.session_state["generated_lines"] = []

# ------------------------------
# Genre Selection
# ------------------------------
st.markdown(
    "<h3 style='color:white; text-align:center;'>Select a Genre</h3>",
    unsafe_allow_html=True
)

genres = ["Fantasy", "Horror", "Mystery", "Sci-Fi", "Romance", "Adventure"]
selected_genre = st.selectbox("Choose Genre:", genres, index=0)
st.session_state["selected_genre"] = selected_genre

# ------------------------------
# Load GPT-Neo 125M model
# ------------------------------
@st.cache_resource(show_spinner=True)
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
    return tokenizer, model

tokenizer, model = load_model()

# ------------------------------
# Generate story helper
# ------------------------------
def generate_story(prompt, max_tokens=150):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(
        input_ids,
        max_length=input_ids.shape[1] + max_tokens,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        top_k=50,
        pad_token_id=tokenizer.eos_token_id
    )
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text[len(prompt):].strip()

# ------------------------------
# Mode Selection
# ------------------------------
st.markdown(
    """
    <style>
    .stRadio>div>label { 
        color: white !important; 
        font-weight: bold;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

mode = st.radio(
    "Choose Mode:",
    ["Interactive Mode", "Full Story Mode"],
    index=0,
    horizontal=True
)

# ------------------------------
# Interactive Mode
# ------------------------------
if mode == "Interactive Mode":
    st.markdown('<h3 style="color:white; text-shadow: 1px 1px 6px rgba(0,0,0,0.8);">Continue your story (Interactive Mode):</h3>', unsafe_allow_html=True)

    characters = st.session_state["characters"]

    # Display current story
    if st.session_state["interactive_story"]:
        st.markdown(
            f"<div class='story-text'>{st.session_state['interactive_story']}</div>",
            unsafe_allow_html=True
        )

    # Input starting prompt if story is empty
    if not st.session_state["interactive_story"]:
        user_prompt = st.text_input("Enter starting prompt:", "")
    else:
        user_prompt = ""

    # Generate next lines
    if st.button("Generate Next Lines"):
        genre = st.session_state["selected_genre"]
        prompt_text = user_prompt if user_prompt else st.session_state["interactive_story"]
        if not prompt_text.strip():
            st.warning("Please enter a starting prompt to generate the story!")
        else:
            full_prompt = (
                f"Write a {genre} story where the protagonist is {characters['main']} "
                f"and the antagonist is {characters.get('villain','')}.\n"
                f"Continue the story: {prompt_text}"
            )
            generated_text = generate_story(full_prompt, max_tokens=100)
            st.session_state["generated_lines"] = [line.strip() for line in generated_text.split('.') if line.strip()]

    # Show radio for selecting next line
    if st.session_state["generated_lines"]:
        st.markdown("<h4 style='color:white;'>Choose the next line to continue:</h4>", unsafe_allow_html=True)
        selected_line = st.radio(
            "",
            st.session_state["generated_lines"]
        )
        if st.button("Add Line to Story"):
            st.session_state["interactive_story"] += selected_line + ". "
            st.session_state["generated_lines"] = []

    # Download button
    if st.session_state["interactive_story"]:
        st.download_button(
            "⬇ Download Story",
            st.session_state["interactive_story"],
            file_name="interactive_story.txt",
            mime="text/plain",
            key="download_interactive"
        )

# ------------------------------
# Full Story Mode
# ------------------------------
else:
    characters = st.session_state["characters"]
    genre = st.session_state["selected_genre"]

    st.markdown(f'<h3 style="color:white; text-shadow: 1px 1px 6px rgba(0,0,0,0.8);">Generating full {genre} story...</h3>', unsafe_allow_html=True)

    if st.button("Generate Full Story"):
        prompt = (
            f"Write a full {genre} story where the protagonist is {characters['main']} "
            f"and the antagonist is {characters.get('villain','')}."
        )
        st.session_state["full_story"] = generate_story(prompt, max_tokens=400)
        st.markdown(f"<div class='story-text'>{st.session_state['full_story']}</div>", unsafe_allow_html=True)

    # Download button
    if st.session_state["full_story"]:
        st.download_button(
            "⬇ Download Full Story",
            st.session_state["full_story"],
            file_name="full_story.txt",
            mime="text/plain",
            key="download_full"
        )
