<b>🎤 Multilingual Grammar Scoring Engine</b>

<i>An AI-powered speech-to-text and grammar analysis tool that can:</i>

<b>Transcribe audio files in Hindi 🇮🇳 & English 🇺🇸.</b>

Translate Hindi to English.

Analyze grammar and provide a grammar score.

<b>🚀 Features</b>

✅ Upload audio (.wav, .mp3, .mp4)✅ Convert audio to text using Speech Recognition✅ Detect and translate Hindi to English (if applicable)✅ Analyze grammar using AI-based grammar checking✅ Provide a grammar score based on errors detected

🛠️ Installation

<b>1️⃣ Clone the Repository</b>

git clone https://github.com/yourusername/multilingual-grammar-engine.git
cd multilingual-grammar-engine

<b>2️⃣ Install Dependencies</b>

Make sure you have Python 3.8+ installed, then run:

pip install -r requirements.txt

<b>3️⃣ Install FFmpeg (for audio conversion)</b>

<b>macOS:</b>

brew install ffmpeg

<b>Ubuntu/Linux:</b>

sudo apt update && sudo apt install ffmpeg

<b>Windows:</b>

Download from FFmpeg official website and add it to PATH.

<b>🎯 How to Use</b>

🔹 Run the App

streamlit run app.py

🔹 Upload an Audio File

1️⃣ Click Browse files and select an .mp3, .mp4, or .wav file.2️⃣ The app converts it to .wav (if needed) and transcribes the text.3️⃣ It detects the language and translates Hindi → English (if necessary).4️⃣ Finally, it checks grammar and gives a score + suggestions.

🛠 Technologies Used

<b>Python 🐍</b>

Streamlit (Web UI)

SpeechRecognition (Transcription)

FFmpeg (Audio Conversion)

Google Translate API (Translation)

LanguageTool (Grammar Analysis)

<b>📝 Example Output</b>

✅ Detected Language: Hindi✅ Transcribed Text: "आज मौसम बहुत अच्छा है।"✅ Translated Text: "The weather is very nice today."✅ Grammar Score: 95/100✅ Suggestions: 1 minor correction

<b>🤝 Contributing</b>

Contributions are welcome! Feel free to fork this repo, open issues, or submit pull requests.

<b>📜 License</b>

This project is licensed under the MIT License – feel free to use and modify it.

⭐ If you like this project, give it a star on GitHub!

<b>🚀 Happy Coding! 🎧</b>

