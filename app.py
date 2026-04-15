import streamlit as st
import pandas as pd
import math

# Configuración con el emoji del pantalón
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖")

# --- ESTILOS CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/denim.png");
        background-color: #1a4175;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px #000000 !important;
    }
    div[data-baseweb="select"], div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 10px !important;
    }
    div[data-testid="stSelectbox"] > div:nth-child(1) > div {
        border: 3px solid #00ff00 !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #000000 !important;
        text-shadow: none !important;
        font-weight: bold !important;
    }
    /* Estilo para las pestañas (Tabs) */
    button[data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 5px 5px 0 0 !important;
        margin-right: 5px !important;
    }
    button[aria-selected="true"] {
        background-color: #00ff00 !important;
        color: black !important;
    }
    .stMetric, .stDataFrame, div[data-testid="stTable"], div[data-testid="stAlert"] {
        background-color: rgba(255, 255, 255, 1) !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    .stMetric * , .stDataFrame * , div[data-testid="stTable"] * , div[data-testid="stAlert"] * {
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

st.markdown('<h1 class="laser-title">👖 Sistema de Gestión de Lavados</h1>', unsafe_allow_html=True)
st.markdown("### Desarrollado por: **Luis Mc**")

# --- BASE DE DATOS BASE (TWIN) ---
# Nombre: [Pzas_por_hora_base, Intensidad, Area]
base_datos = {
    "MYYA": [70, "45%", "LÁSER"],
    "BLGU": [50, "45%", "LÁSER"],
    "ZRCN": [56, "45%", "LÁSER"],
    "BFOW": [43, "45%", "LÁSER"],
    "DELT": [40, "45%", "LÁSER"],
    "MOBU": [43, "45%", "LÁSER"],
    "BLUV": [50, "45%", "LÁSER"],
    "RGRI": [45, "45%", "LÁSER"],
    "OVRW": [43, "45%", "LÁSER"],
    "DSP1": [43, "45%", "LÁSER"],
    "CUMB": [43, "45%", "LÁSER"],
    "ALPA": [54, "45%", "LÁSER"],
    "CTBU": [45, "45%", "LÁSER"],
    "JAIL": [0, "SUAVIZADO", "LAVANDERÍA"],
    "OEDW": [0, "TEÑIDO", "LAVANDERÍA"],
    "STONE": [0, "DESLAVE", "LAVANDERÍA"]
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o selecciona un código:", ["-- Selecciona un lavado --"] + opciones)

if seleccion != "-- Selecciona un lavado --":
    datos = base_datos[seleccion]
    pzas_hora_base = datos[0]
    info_extra = datos[1]
    area = datos[2]
    
    st.divider()
    
    if area == "LÁSER":
        st.subheader(f"📊 Reporte de Producción: {seleccion}")
        
        # CREACIÓN DE PESTAÑAS PARA LAS MÁQUINAS
        tab1, tab2, tab3 = st.tabs(["✳️ TWIN (Maniquí)", "❇️ FLEXI (Maniquí)", "✴️ FLEXI (Mesa)"])
        
        # Función para mostrar los cálculos
        def mostrar_calculos(pzas_hora):
            segundos = int(3600 / pzas_hora)
            minutos = segundos // 60
            seg_rest = segundos % 60
            tiempo_txt = f"{minutos} min {seg_rest} seg ({segundos} seg)"
            
            c1, c2 = st.columns(2)
            with c1: st.metric("Tiempo por Prenda", tiempo_txt)
            with c2: st.metric("Prod. por Hora", f"{pzas_hora} pzas")
            
            st.markdown("**Capacidad por Jornada:**")
            horas = [8, 10, 12]
            df = pd.DataFrame({
                "Horas": [f"{h}h" for h in horas],
                "Total Prendas": [f"{h * pzas_hora} pzas" for h in horas]
            })
            st.table(df)

        with tab1:
            st.write("### Sistema Twin Doble Cañón")
            mostrar_calculos(pzas_hora_base)

        with tab2:
            st.write("### Sistema Flexi Maniquí (Alta Velocidad)")
            mostrar_calculos(pzas_hora_base + 8)

        with tab3:
            st.write("### Sistema Flexi Mesa (Manual)")
            mostrar_calculos(pzas_hora_base - 5)
            
    else:
        st.subheader(f"🧼 Detalle Lavandería: {seleccion}")
        st.info(f"📍 Área: {area} | ⚙️ Proceso: {info_extra}")

st.sidebar.markdown("---")
st.sidebar.write(f"✅ Lavado actual: {seleccion}")
