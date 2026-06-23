import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# load the env file because I don't want to upload my key to github again
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY", "")

def generate_copy(prompt, temperature=0.9, top_p=0.95):
    # check if the api key actually exists
    if not API_KEY:
        print("Error: GEMINI_API_KEY not found. Add it to your .env file.")
        return None

    try:
        # trying out the new gemini sdk
        client = genai.Client(api_key=API_KEY)
        
        # pass the settings
        config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=top_p,
        )

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
            config=config
        )
        return response.text
        
    except Exception as e:
        # FIXME: sometimes it crashes if my internet drops, need to handle this better
        print(f"API Error: {e}")
        return None
