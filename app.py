import streamlit as st
import speech_recognition as sr
import language_tool_python
import os
import tempfile
import subprocess
from googletrans import Translator
from langdetect import detect

# Initialize tools
tool = language_tool_python.LanguageTool('en-US')
translator = Translator()

# Page Configuration
st.set_page_config(page_title="Multilingual Grammar Checker", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <h1>🧠 Multilingual Grammar Scoring Engine 🎤</h1>
        <h4>🎵 Transcribe | 🌐 Translate | ✅ Analyze</h4>
        <p style='color:gray;'>Supports Hindi 🇮🇳 and English 🇺🇸 audio (.wav, .mp3, .mp4)</p>
    </div>
""", unsafe_allow_html=True)

# Upload Section
st.markdown("### 📂 Upload Your Audio File (.wav, .mp3, .mp4)")
uploaded_file = st.file_uploader("", type=["wav", "mp3", "mp4"])

if uploaded_file:
    file_extension = os.path.splitext(uploaded_file.name)[1]

    # Create a temporary file with the uploaded file's extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Convert MP3/MP4 to WAV if necessary
    if file_extension.lower() in [".mp3", ".mp4"]:
        converted_wav_path = temp_file_path.replace(file_extension, ".wav")

        st.info("🎵 Converting file to WAV format...")
        try:
            subprocess.run(["ffmpeg", "-i", temp_file_path, converted_wav_path, "-y"], check=True)
            temp_file_path = converted_wav_path  # Use the converted file for recognition
        except subprocess.CalledProcessError:
            st.error("⚠️ Error: Failed to convert audio file. Ensure FFmpeg is installed.")
            os.remove(temp_file_path)
            st.stop()

    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(temp_file_path) as source:
            st.info("🎙️ Listening to the audio...")
            audio = recognizer.record(source)

            # Try recognizing speech
            try:
                transcript = recognizer.recognize_google(audio, language="hi-IN")
                st.success("✅ Transcription Completed!")
            except sr.UnknownValueError:
                st.warning("🔄 Speech could not be recognized. Try uploading a clearer audio file.")
                transcript = None
            except sr.RequestError as e:
                st.error(f"⚠️ API request failed. Please check your internet connection. Error: {e}")
                transcript = None
            except Exception as e:
                st.error(f"⚠️ Unexpected error during transcription: {e}")
                transcript = None

        # Proceed only if transcription was successful
        if transcript:
            st.markdown("#### 📝 Original Transcript")
            st.code(transcript)

            # Detect language
            detected_lang = detect(transcript)
            st.markdown(f"#### 🌐 Detected Language: `{detected_lang.upper()}`")

            if detected_lang != "en":
                st.info("🔁 Translating to English...")
                translated = translator.translate(transcript, src=detected_lang, dest='en').text
                st.markdown("#### 🌍 Translated Text (English)")
                st.code(translated)
                text_to_check = translated
            else:
                text_to_check = transcript

            # Grammar Check
            st.markdown("### 🛠 Grammar Analysis")
            matches = tool.check(text_to_check)
            error_count = len(matches)
            grammar_score = max(100 - (error_count * 5), 0)

            # Score Display
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📊 Grammar Score", f"{grammar_score}/100")
            with col2:
                st.metric("❌ Grammar Errors", error_count)

            if matches:
                st.markdown("### 🧾 Suggestions")
                for match in matches:
                    st.write(f"**❌ Error:** {match.context}")
                    st.write(f"**💡 Suggestion:** {', '.join(match.replacements)}")
                    st.markdown("---")

    except FileNotFoundError:
        st.error(f"❌ File not found: {temp_file_path}. Ensure the file was uploaded correctly.")
    except sr.AudioFile as e:
        st.error(f"⚠️ Could not process the audio file: {e}")
    except Exception as e:
        st.error(f"⚠️ Unexpected error: {e}")
    finally:
        # Cleanup temporary files
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        if file_extension.lower() in [".mp3", ".mp4"] and os.path.exists(converted_wav_path):
            os.remove(converted_wav_path)