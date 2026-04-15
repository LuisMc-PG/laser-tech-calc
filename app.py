import streamlit as st
import pandas as pd
import math

# Configuración con el emoji del pantalón
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖")

# --- ESTILOS CSS REFORZADOS ---
st.markdown(
    """
    <style>
    /* Fondo de mezclilla */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/denim.png");
        background-color: #1a4175;
        background-attachment: fixed;
    }

    /* Contraste extremo para textos fuera de cuadros */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px #000000 !important;
        font-weight: bold !important;
    }

    /* Cuadros de métricas y tablas con fondo sólido para lectura fácil */
    [data-testid="stMetric"], .stDataFrame, div[data-testid="stTable"], .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 1) !important;
        border-radius: 10px !important;
        padding: 5px;
    }

    /* Forzar texto oscuro dentro de los cuadros blancos */
    [data-testid="stMetric"] div, .stDataFrame div, td, th, div[role="listbox"] {
        color: #1a4175 !important;
        text-shadow: none !important;
    }
    
    .laser-title {
        color: #00ff00 !important;
        text-shadow: 0 0 15px #00ff00 !important;
        font-family: 'Courier New', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO CON PANTALÓN ---
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
    "OEDW": [0, "TEÑIDO", "LAVANDERÍA"],
    "STONE": [0, "DESLAVE", "LAVANDERÍA"]
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o selecciona un código:", ["-- Selecciona un lavado --"] + opciones)

if seleccion != "-- Selecciona un lavado --":
    datos = base_datos[seleccion]
    segundos_totales = datos[0]
    info_extra = datos[1]
    area = datos[2]
    
    st.divider()
    
    if area == "LÁSER":
        st.subheader(f"👖 Detalle Láser: {seleccion}")
        
        minutos = segundos_totales // 60
        segundos_rest = segundos_totales % 60
        tiempo_texto = f"{minutos} min {segundos_rest} seg ({segundos_totales} seg)"
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tiempo de Marcado", tiempo_texto)
        with col2:
            st.metric("Intensidad", info_extra)
            
        st.markdown("#### 🕒 Producción Estimada")
        horas = [8, 10, 12, 24]
        produccion = [math.floor((h * 3600) / segundos_totales) for h in horas]
        
        df = pd.DataFrame({
            "Turno": [f"{h} Horas" for h in horas],
            "Capacidad": [f"{p} prendas" for p in produccion]
        })
        st.table(df)
        
    else:
        st.subheader(f"🧼 Detalle Lavandería: {seleccion}")
        st.info(f"📍 Área: {area} | ⚙️ Proceso: {info_extra}")

st.sidebar.markdown("---")
st.sidebar.write("✅ Base de Datos Lista")
