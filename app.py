import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import requests

# Función para cargar animaciones Lottie desde una URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Estilos para fondo negro y texto blanco
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    textarea, .stTextInput>div>div>input {
        background-color: #333333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    <div style='color:white'>
    <b>Polaridad:</b> Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    <br><br>
    <b>Subjetividad:</b> Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    </div>
    """, unsafe_allow_html=True)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polaridad:', polarity)
        st.write('Subjetividad:', subjectivity)

        if polarity >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_happy.json")
            st_lottie(animation, width=350)
        elif polarity <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_sad.json")
            st_lottie(animation, width=350)
        else:
            st.write('Es un sentimiento Neutral 😐')
            animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_neutral.json")
            st_lottie(animation, width=350)
