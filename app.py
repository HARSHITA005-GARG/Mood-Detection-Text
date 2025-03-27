import streamlit as st
from mood_detection import predict_mood, recognize_speech
import os
from flask import Flask

app = Flask(__name__)

# Health Check Route
@app.route('/health')
def health_check():
    return "OK", 200

# Run Streamlit
def run_streamlit():
    os.system("streamlit run app.py --server.port=8000 --server.address=0.0.0.0")

def main():
    st.title("Mood Detection App with Speech-to-Text 🎙️😊")

    # Choose Input Method
    st.write("Choose your preferred input method:")
    input_method = st.radio("Select Input Method", ["Text", "Speech"])

    # Handle Text Input
    user_input = ""
    if input_method == "Text":
        user_input = st.text_area("Enter your text here", height=150)

    # Handle Speech Input
    elif input_method == "Speech":
        if st.button("Record Speech"):
            st.write("Recording... Speak now!")
            user_input = recognize_speech()
            if not user_input:
                st.error("Speech recognition failed. Please try again.")
            else:
                st.success("Speech recognized successfully!")

    # Perform Mood Prediction
    if user_input.strip():
        st.subheader("Detected Moods:")
        moods = predict_mood(user_input)

        if moods:
            for mood, emoji, score in moods:
                st.write(f"**Mood:** {mood} {emoji} - Confidence: {score:.2f}")
        else:
            st.info("No significant moods detected. Try with a different input.")
    else:
        st.warning("Please enter text or speak to analyze your mood.")

if __name__ == "__main__":
    from threading import Thread
    t = Thread(target=run_streamlit)
    t.start()
    app.run(host="0.0.0.0", port=8000)
