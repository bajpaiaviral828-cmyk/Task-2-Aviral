# Copywriting & Tone Transformer

### 🚀 Live Demo (No installation required!)
You don't need to install anything to try this out. Just click the link below to open the Web UI right in your browser!

👉 **[Try the Live Demo Here](https://raw.githack.com/bajpaiaviral828-cmyk/copywriting-tone-transformer/main/demo.html?v=2)**

This is a Python project I built to learn more about Prompt Engineering and the Gemini API. 

## Why I Built This
Writing LinkedIn posts, emails, and tweets takes forever because they all have different rules. A tweet has to be short, an email needs a subject line, and LinkedIn needs professional hooks. I wanted to see if I could write a Python script that takes one idea and automatically rewrites it for different platforms by injecting specific rules into an f-string prompt.

## What I Learned
- **Prompt Templates:** I learned how to use Python f-strings to dynamically insert "platform rules" and "tone rules" into a master prompt before sending it to the AI.
- **Data Validation:** I used Pydantic (which I found in a YouTube tutorial) to validate user inputs so the script doesn't crash if someone types "MySpace" as the platform.
- **Rate Limits:** When I tried to run a batch CSV file, Google kept blocking me. I had to learn how to use a basic `time.sleep()` loop to slow down the requests.

## How to use it

1. Make sure you have python installed.
2. Install the libraries: `pip install -r requirements.txt`
3. Add your Gemini API key to `.env`
4. Run it from the terminal:
```bash
python main.py --name "Smart Coffee" --desc "A mug that keeps your coffee hot." --platform "twitter" --tone "funny"
```

## Demo
There is a `demo.html` file in this folder. You can open it in your browser to try it out visually. 
*(Note: I put the API call directly in the HTML file for testing. If this was a real production app, I would need to build a backend server to hide the API key).*

## TODOs
- [ ] Add more platforms like TikTok scripts.
- [ ] Make the batch processor faster (it takes forever with time.sleep).
- [ ] Save the generated copy to a database instead of just printing it.
