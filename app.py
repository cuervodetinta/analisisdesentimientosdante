import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Estilos para fondo negro y texto blanco, y personalización del sidebar
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
    
    /* Personalización del sidebar */
    .css-18e3th9 {
        background-color: #ffb6c1;  /* Rosado clarito */
    }
    .css-18e3th9 .sidebar-content {
        color: #c71585;  /* Rosado oscuro para el texto */
    }
    .css-1v3fvcr {
        color: #c71585;  /* Rosado oscuro para los encabezados del sidebar */
    }

    .sidebar .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

translator = Translator()
st.title('Uso de textblob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    # Cargar imagen "wawawa.png" en el sidebar
    st.image('wawawa.png', use_column_width=True)
    
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    <div style='color:#c71585'>
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

        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        if polarity >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            with open('feliz.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
        elif polarity <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            with open('triste.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
        else:
            st.write('Es un sentimiento Neutral 😐')
            with open('neutral.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
