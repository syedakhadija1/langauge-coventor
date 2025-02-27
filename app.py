import streamlit as st
import googletrans
from googletrans import Translator
import time
from gtts import gTTS
import os
import pyperclip

# Initialize Translator
translator = Translator()

# Streamlit App Title with Cyberpunk Neon Styling
st.set_page_config(page_title="Language Converter", page_icon="🌍", layout="wide")

# Custom CSS for Cyberpunk Neon Theme
st.markdown(
    """
   <style>
    body {
        background: linear-gradient(135deg, #0f0c29, #1a1a2e);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #5a0271; /* Pink Color */
        background: #d3d3d3; /* Grey Background */
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        animation: glow 2s infinite alternate, float 3s ease-in-out infinite;
    }

    @keyframes glow {
        0% { text-shadow: 0 0 5px #00ffcc, 0 0 10px #00ccff; }
        100% { text-shadow: 0 0 20px #00ffcc, 0 0 30px #00ccff; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .translate-button {
        background: linear-gradient(90deg, #00ffcc, #00ccff);
        color: #0f0c29;
        font-size: 20px;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 10px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 0 10px #00ffcc, 0 0 20px #00ccff;
        animation: pulse 1.5s infinite;
    }

    .translate-button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #00ffcc, 0 0 30px #00ccff;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.5);
        background-color: #d3d3d3; /* Light Grey Background */
        color: #5a0271; /* Dark Purple Text */
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        backdrop-filter: blur(10px);
        animation: slideIn 1s ease-out;
    }

    .stSelectbox select {
        background-color: rgba(0, 0, 0, 0.5);
        color: #00ffcc; /* Neon cyan for dropdown text */
        border: 2px solid #00ffcc; /* Neon cyan border */
        border-radius: 10px;
        padding: 8px;
        font-size: 16px;
        backdrop-filter: blur(10px);
        animation: slideIn 1s ease-out;
    }

    .stSuccess {
        background: #d3d3d3;
        color: #00ffcc; /* Neon cyan for success text */
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #00ffcc; /* Neon cyan border */
        animation: fadeIn 1s ease-in-out, bounce 1s ease-in-out;
    }

    .stWarning {
        background-color: rgba(255, 0, 102, 0.1);
        color: #ff0066; /* Pink for warning text */
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #ff0066; /* Pink border */
        animation: fadeIn 1s ease-in-out, shake 0.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        50% { transform: translateX(10px); }
        75% { transform: translateX(-10px); }
    }

    .footer {
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #5a0271; /* Darker Pinkish-Purple */
        margin-top: 30px;
        padding: 12px;
        background: linear-gradient(90deg, #e0e0e0, #d3d3d3); /* Light Grey Gradient */
        border-radius: 12px;
        animation: fadeIn 1.5s ease-in-out, float 3s ease-in-out infinite;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        letter-spacing: 1px;
    }

    .sidebar .sidebar-content {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        animation: slideIn 1s ease-out, glowSidebar 3s infinite alternate;
    }

    @keyframes glowSidebar {
        0% { box-shadow: 0 0 5px #00ffcc, 0 0 10px #00ccff; }
        100% { box-shadow: 0 0 20px #00ffcc, 0 0 30px #00ccff; }
    }

    .sidebar .sidebar-content h2 {
        color: #ffffff;
        font-size: 22px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
        animation: fadeIn 1s ease-in-out, float 3s ease-in-out infinite;
    }

    .sidebar .stSelectbox {
        background-color: white;
        border-radius: 5px;
        animation: slideIn 1s ease-out;
    }

    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .special-heading {
        font-size: 36px;
        font-weight: bold;
        color: #5a0271; /* Pink Color */
        background: #d3d3d3; /* Grey Background */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        animation: glow 2s infinite alternate, float 3s ease-in-out infinite;
    }

    .special-subheading {
        font-size: 24px;
        font-weight: bold;
        color: #5a0271; /* Pink Color */
        margin-bottom: 15px;
        animation: fadeIn 1s ease-in-out;
    }

    .glassmorphism {
        background: #d3d3d3;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        animation: slideIn 1s ease-out;
    }

    /* New Style for Country & Language Selector */
    .country-language-selector {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #5a0271; /* Pink Color */
        background: #d3d3d3; /* Grey Background */
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        animation: glow 2s infinite alternate, float 3s ease-in-out infinite;
    }
</style>
    """,
    unsafe_allow_html=True,
)

# Country Flags Mapping
country_flags = {
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Belgium": "🇧🇪",
    "Brazil": "🇧🇷",
    "Bulgaria": "🇧🇬",
    "Canada": "🇨🇦",
    "Croatia": "🇭🇷",
    "Cyprus": "🇨🇾",
    "Czech Republic": "🇨🇿",
    "Denmark": "🇩🇰",
    "Estonia": "🇪🇪",
    "Finland": "🇫🇮",
    "France": "🇫🇷",
    "Germany": "🇩🇪",
    "Gibraltar": "🇬🇮",
    "Greece": "🇬🇷",
    "Hong Kong": "🇭🇰",
    "Hungary": "🇭🇺",
    "India": "🇮🇳",
    "Ireland": "🇮🇪",
    "Italy": "🇮🇹",
    "Japan": "🇯🇵",
    "Latvia": "🇱🇻",
    "Liechtenstein": "🇱🇮",
    "Lithuania": "🇱🇹",
    "Luxembourg": "🇱🇺",
    "Malaysia": "🇲🇾",
    "Malta": "🇲🇹",
    "Mexico": "🇲🇽",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Norway": "🇳🇴",
    "Poland": "🇵🇱",
    "Portugal": "🇵🇹",
    "Romania": "🇷🇴",
    "Singapore": "🇸🇬",
    "Slovakia": "🇸🇰",
    "Slovenia": "🇸🇮",
    "Spain": "🇪🇸",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧",
    "United States": "🇺🇸",
}

# Sidebar Content
st.sidebar.title("🌍 Country & Language Selector")

# Country Selection with Flags
st.sidebar.markdown("### Select Your Country")
countries = list(country_flags.keys())
selected_country = st.sidebar.selectbox(
    "", 
    countries, 
    index=countries.index("United States"), 
    format_func=lambda x: f"{country_flags[x]} {x}"  # Display flag + country name
)

# Language Selection
st.sidebar.markdown("### Select Your Language")
languages = ["English (United States)", "German (Germany)", "French (France)", "Spanish (Spain)"]
selected_language = st.sidebar.selectbox("", languages, index=languages.index("English (United States)"))

# Request Invite Button
if st.sidebar.button("Request an Invite"):
    st.sidebar.success("Your request has been submitted!")

# Additional Links
st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Links")
st.sidebar.markdown("- [Atlas](#)")
st.sidebar.markdown("- [Billing](#)")
st.sidebar.markdown("- [Capital](#)")
st.sidebar.markdown("- [Developers](#)")
st.sidebar.markdown("- [Documentation](#)")
st.sidebar.markdown("- [API Reference](#)")
st.sidebar.markdown("- [API Status](#)")

# Main Content
st.markdown("<div class='main-title'>Language Converter🌍</div>", unsafe_allow_html=True)
st.markdown("<div class='special-heading'>Easily Convert Text Between Multiple Languages</div>", unsafe_allow_html=True)

# User Input with Modern UI
st.markdown("<div class='special-subheading'>📝 Enter Text Below:</div>", unsafe_allow_html=True)
text = st.text_area("", height=150, placeholder="Type or paste your text here...")

# Language Selection for Translation
languages = googletrans.LANGUAGES
language_options = list(languages.values())
target_lang_name = st.selectbox("🌐 Select Target Language:", language_options, index=language_options.index("english"))

# Detect Language Button
if st.button("🔍 Detect Language", key="detect_btn"):
    if text.strip():
        detected_lang = translator.detect(text).lang
        detected_lang_name = languages.get(detected_lang, "Unknown")
        st.info(f"**Detected Language:** {detected_lang_name.capitalize()} ({detected_lang})")
    else:
        st.warning("Please enter some text to detect the language.")

# Get language code
target_lang_code = [key for key, value in languages.items() if value == target_lang_name][0]

# Translation Button with Animated UI
if st.button("🌍 Translate", key="translate_btn"):
    if text.strip():
        with st.spinner("Translating... Please wait..."):
            time.sleep(1)  # Simulating processing delay
            translated_text = translator.translate(text, dest=target_lang_code).text
            st.success(f"**Translated Text:** {translated_text}")
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.markdown("<div class='footer'> Made with ❤️ by Syeda Khadija Abrar | Language Translator</div>", unsafe_allow_html=True)