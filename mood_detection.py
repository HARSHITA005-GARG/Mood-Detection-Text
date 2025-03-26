import streamlit as st 
import speech_recognition as sr
from transformers import pipeline
import spacy
import subprocess

def load_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
        print("SpaCy model loaded successfully.")
    except OSError:
        print("SpaCy model not found. Downloading 'en_core_web_sm'...")
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        nlp = spacy.load("en_core_web_sm")
        print("Download complete. Model loaded.")
    return nlp

nlp = load_spacy_model()

# Load your emotion classifier
classifier = pipeline("text-classification", 
                       model="SamLowe/roberta-base-go_emotions", 
                       top_k=None)
print(classifier.model.config.id2label)
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        try:
            audio_data = recognizer.listen(source, timeout=5)
            st.info("Recognizing speech...")
            text = recognizer.recognize_google(audio_data)
            st.success(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            st.warning("Speech recognition timed out. Please try again.")
            return None
        except sr.UnknownValueError:
            st.warning("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError:
            st.error("There was an issue with the speech recognition service.")
            return None

def get_emoji(label):
    emoji_mapping = {
        "admiration": "👏",
        "amusement": "😂",
        "anger": "😡",
        "annoyance": "😠",
        "approval": "👍",
        "caring": "🤗",
        "confusion": "😕",
        "curiosity": "🤔",
        "desire": "😍",
        "disappointment": "😞",
        "disapproval": "👎",
        "disgust": "🤢",
        "embarrassment": "😳",
        "excitement": "🤩",
        "fear": "😨",
        "gratitude": "🙏",
        "grief": "😭",
        "joy": "😊",
        "love": "❤️",
        "nervousness": "😰",
        "optimism": "🌟",
        "pride": "🥳",
        "realization": "💡",
        "relief": "😌",
        "remorse": "😔",
        "sadness": "😢",
        "surprise": "😮",
        "neutral": "😐"
    }
    return emoji_mapping.get(label.lower(), "❓")


def predict_mood(text, max_emotions=4, threshold=0.05):
    results = classifier(text)
    results = sorted(results[0], key=lambda x: x['score'], reverse=True)

    moods = []
    for result in results[:max_emotions]:
        label = result['label']
        score = result['score']
        if score >= threshold:
            emoji = get_emoji(label)
            moods.append((label, emoji, score))
    return moods



text = "Wow! I didn't see that coming. It was totally unexpected. I am so happy now!"
moods = predict_mood(text)
print(moods)
