import logging
from google.generativeai import configure
import google.generativeai as genai
from dotenv import load_dotenv
import os
from common_imports import gemini_model

# Load environment variables
load_dotenv()

# Configure the Gemini API
configure(api_key=os.getenv("GEMINI_API_KEY")) 

def generate_gemini_response(prompt, model=gemini_model):
    try:
        model = genai.GenerativeModel(model)

        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        logging.error(f"Error generating Gemini response: {e}")
        return f"An error occurred: {e}"