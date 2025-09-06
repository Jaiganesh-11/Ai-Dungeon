# 🌌 DreamWeaver AI

**DreamWeaver AI** is an interactive story-generation web app built with **Streamlit** and **GPT-Neo**.  
It transforms your imagination into unique stories by letting you pick genres, create characters, and guide the narrative.

---

## ✨ Features
- 🎭 **Pick a Genre**: Fantasy, Sci-Fi, Horror, Adventure, Romance, Mystery  
- 🧑‍🤝‍🧑 **Create Characters**: Define protagonist and antagonist  
- 📖 **Two Story Modes**:  
  - *Interactive Mode*: Continue story step-by-step with AI suggestions  
  - *Full Story Mode*: Generate a complete story in one go  
- 🎨 **Custom UI**: Immersive design with background images, styled buttons, and genre cards  
- ⚡ **Efficient AI**: Uses cached GPT-Neo model for smooth performance  
- 💾 **Download Option**: Save your generated story locally  

---

## 🛠️ Tech Stack
- **Frontend & App**: [Streamlit](https://streamlit.io/)  
- **AI Model**: [Hugging Face Transformers](https://huggingface.co/transformers) – GPT-Neo 125M  
- **Backend**: Python 3.10+  
- **Styling**: Custom CSS + embedded background images (Base64 encoding)  

---

## 🎯 Project Flow
- **Home Page → Play button → Menu**
- **Menu → Select genre → Next**
- **Character Page → Define characters → Continue**
- **Story Page → Choose mode → Generate story**

---

## 💡 How It Works
- **Uses Streamlit session state to carry user choices across pages**
- **Loads GPT-Neo 125M via Hugging Face with @st.cache_resource to avoid reloading**
- **Sampling controls (temperature, top_p, top_k) tune story creativity and coherence**
- **Stories can be downloaded as .txt files**

---

## 📌 Future Improvements
- **Add more story genres**
- **Support long-form story saving**
- **Enhance UI animations and interactivity**
- **Deploy online via Streamlit Cloud / Hugging Face Spaces**

---

## 👨‍💻 Author
- **Developed with ❤️ using Python, Streamlit, and AI.**

## 📌 Explanation:
- **streamlit → The framework for building the interactive web app**
- **transformers → Provides GPT-Neo model and tokenizer**
- **torch → Backend deep learning library required by GPT-Neo**
- **Pillow → Used for image handling (placeholders/screenshots, etc.)**
