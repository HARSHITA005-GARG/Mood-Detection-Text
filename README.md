# 🧠 Mood Detection App

A web-based application that detects emotions from user input text or speech using a Natural Language Processing (NLP) model. Built using **Streamlit** for the frontend and **Hugging Face Transformers** for mood detection.  

---

## 🚀 Features

- Detects multiple emotions from text using **SamLowe/roberta-base-go_emotions**.  
- Supports both **text input** and **speech recognition**.  
- Displays detected emotions with **confidence scores** and relevant **emojis**.  

---

## 🛠️ Tech Stack

- **Python**  
- **Streamlit**  
- **Hugging Face Transformers**  
- **SpeechRecognition** (for voice input)  
- **SpaCy** (for sentence tokenization)  

---

## 📦 Installation

1. **Clone the Repository:**  
    ```bash
    git clone https://github.com/HARSHITA005-GARG/Mood-Detection-Text.git
    cd Mood-Detection-Text
    ```

2. **Create and Activate Virtual Environment:**  
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Linux/macOS
    venv\Scripts\activate       # On Windows
    ```

3. **Install Dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Download SpaCy Model:**  
    ```bash
    python -m spacy download en_core_web_sm
    ```

---

## 🧑‍💻 Usage

1. Run the Streamlit app:  
    ```bash
    streamlit run app.py
    ```

2. Open the link displayed in the terminal (e.g., `http://localhost:8501`).  

3. Choose between **Text Input** or **Speech Input**.  

4. View your mood predictions with emojis and confidence scores.  

---

## ⚡ Example Test Sentences

Try these sample sentences to test the model:  

1. _"I am so excited for my birthday party tomorrow!"_ 🎉  
2. _"I can't believe she forgot my birthday, it makes me so sad."_ 😔  
3. _"The roller coaster was thrilling and scary at the same time."_ 🎢😱  
4. _"I admire your determination and courage."_ 💪👏  
5. _"I love spending time with my family."_ ❤️  

---

## 🐛 Troubleshooting

- **Speech not recognized?**  
  Ensure your microphone is enabled and permissions are granted.  

- **Incorrect mood predictions?**  
  The model may have limitations on nuanced emotions or complex sentences.  

- **Errors in SpaCy?**  
  Ensure `en_core_web_sm` is downloaded:  
  ```bash
  python -m spacy download en_core_web_sm
