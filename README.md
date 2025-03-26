# Mood Detection from Text

A simple web application that detects the mood from a given text input using Natural Language Processing (NLP). This project is built using **Streamlit** for the frontend and **SpaCy** for NLP processing. It also supports speech-to-text input for a more interactive experience.

## 🌟 Features

- Detects mood from user input text using SpaCy
- Supports speech recognition for hands-free input
- Interactive and user-friendly interface using Streamlit
- Lightweight and easy to deploy using Docker

## 🚀 Live Demo

You can access the deployed application here:  
[**Mood Detection App on Render**](https://mood-detection-text.onrender.com)

## 🛠️ Technologies Used

- **Python 3.12**  
- **Streamlit** for UI  
- **SpaCy** for Natural Language Processing  
- **SpeechRecognition** for speech input  
- **Docker** for containerization  

## 🧑‍💻 Installation Guide

Follow these steps to set up the project locally:

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/HARSHITA005-GARG/Mood-Detection-Text.git
    cd Mood-Detection-Text
    ```

2. **Create a Virtual Environment**  
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Download SpaCy Model**  
    ```bash
    python -m spacy download en_core_web_sm
    ```

5. **Run the Application**  
    ```bash
    streamlit run app.py
    ```

6. **Access the App**  
    - Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Deploy Using Docker

To build and run the app using Docker, follow these steps:

1. **Build the Docker Image**  
    ```bash
    docker build -t mood-detection-app .
    ```

2. **Run the Container**  
    ```bash
    docker run -p 8501:8501 mood-detection-app
    ```

3. **Access the App**  
    - Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🛡️ License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open an issue or submit a pull request on the [GitHub Repository](https://github.com/HARSHITA005-GARG/Mood-Detection-Text).  

---

## 📧 Contact

- **GitHub**: [HARSHITA005-GARG](https://github.com/HARSHITA005-GARG)   

---

**Enjoy using the Mood Detection App! 😊**  
