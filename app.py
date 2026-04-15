import streamlit as st
import pandas as pd
import math

# Configuración con el emoji del pantalón
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖")

# --- ESTILOS CSS REFORZADOS ---
st.markdown(
    """
    <style>
    /* 1. Fondo de mezclilla */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/denim.png");
        background-color: #1a4175;
        background-attachment: fixed;
    }

    /* 2. Texto general en blanco */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px #000000 !important;
    }

    /* 3. EL BUSCADOR (SELECTBOX) - BLANCO PURO */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important; /* Blanco puro */
        border-radius: 10px !important;
        border: 3px solid #00ff00 !important; /* Borde neón */
    }
    
    /* Texto dentro del buscador (Negro para contraste total) */
    div[data-baseweb="select"] * {
        color: #000000 !important;
        text-shadow: none !important;
        font-weight: bold !important;
    }

    /* 4. Cuadros de resultados (Métricas y Tablas) */
    [data-testid="stMetric"], 
    .stDataFrame, 
    div[data-testid="stTable"],
    div[data-testid="stAlert"] {
        background-color: rgba(255, 255, 255, 1) !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Texto oscuro dentro de resultados */
    [data-testid="stMetric"] * , 
    .stDataFrame * , 
    div[data-testid="stTable"] * , 
    div[data-testid="stAlert"] * {
        color: #1a4175 !important;
        text-shadow: none !important;
    }

    /* 5. Título neón */
    .laser-title {
        color: #00ff00 !important;
        text-shadow: 0 0 15px #00ff00 !important;
        font-family: 'Courier New', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO ---
st.markdown('<h1 class="laser-title">👖 Sistema de Gestión de Lavados</h1>', unsafe_allow_html=True)
st.markdown("### Desarrollado por: **Luis Mc**")

# --- BASE DE DATOS ---
base_datos = {
    "MYYA": [51, "45%", "LÁSER"],
    "BLGU": [72, "45%", "LÁSER"],
    "ZRCN": [64, "45%", "LÁSER"],
    "BFOW": [84, "45%", "LÁSER"],
    "DELT": [90, "45%", "LÁSER"],
    "MOBU": [84, "45%", "LÁSER"],
    "BLUV": [72, "45%", "LÁSER"],
    "RGRI": [80, "45%", "LÁSER"],
    "OVRW": [84, "45%", "LÁSER"],
    "DSP1": [84, "45%", "LÁSER"],
    "CUMB": [84, "45%", "LÁSER"],
    "ALPA": [67, "45%", "LÁSER"],
    "CTBU": [80, "45%", "LÁSER"],
    "JAIL": [0, "SUAVIZADO", "LAVANDERÍA"],
    "OED
