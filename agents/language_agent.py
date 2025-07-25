import os
import google.generativeai as genai
from dotenv import load_dotenv



api_key =""

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemma-3-27b-it")

def generate_market_brief(data_dict, earnings):
    prompt = f"""Generate a financial market brief in plain English.
    Portfolio exposure: {data_dict}
    Earnings updates: {earnings}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini API Error:", e)
        return "Sorry, there was an error generating the market brief."
