import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load the Gemini API key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ Missing Google Gemini API key in .env file.")

# ✅ Configure the Gemini client
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Correct full model name (required)
model = genai.GenerativeModel("gemini-2.5-flash")

def clean_text(text):
    cleaned = re.sub(r'\s+', ' ', text)  # Collapse multiple spaces
    cleaned = re.sub(r'[^\x00-\x7F]+', ' ', cleaned)  # Remove non-ASCII
    return cleaned.strip()

def summarize_text(text):
    print("✨ Generating summary using Gemini...")

    try:
        cleaned = clean_text(text)
        prompt = f"Summarize this text clearly in a few sentences:\n\n{cleaned[:4000]}"

        # ✅ Use the correct method
        response = model.generate_content(prompt)

        if response and hasattr(response, 'text'):
            return response.text
        else:
            print("⚠️ No summary returned.")
            return None

    except Exception as e:
        print("❌ Gemini error:", e)
        return None

