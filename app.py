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

# --- BASE DE DATOS BASE ---
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

# --- DICCIONARIO DE FORMULAS (EJEMPLO DELT) ---
formulas = {
    "DELT": [
        {"Paso": "Desengome", "Temp": "50°C", "Tiempo": "12 min", "Químicos": "Humectante, Amilasa"},
        {"Paso": "Abrasión (Stone)", "Temp": "40°C", "Tiempo": "35 min", "Químicos": "Piedra Pómez, Enzima"},
        {"Paso": "Bajada de Tono", "Temp": "40°C", "Tiempo": "5 min", "Químicos": "Cloro (5.0 KG)"},
        {"Paso": "Neutralizado", "Temp": "Frío", "Tiempo": "4 min", "Químicos": "Bisulfito (2.0 KG)"},
        {"Paso": "Suavizado", "Temp": "40°C", "Tiempo": "10 min", "Químicos": "Suavizante Mac, Silicon"}
    ]
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o selecciona un código:", ["-- Selecciona un lavado --"] + opciones)

if seleccion != "-- Selecciona un lavado --":
    datos = base_datos[seleccion]
    pzas_hora_base = datos[0]
    area = datos[2]
    
    st.divider()
    
    if area == "LÁSER":
        st.subheader(f"📊 Reporte de Producción: {seleccion}")
        
        # PESTAÑAS: Twin, Flexi M, Flexi Mesa + FÓRMULA
        tab1, tab2, tab3, tab4 = st.tabs(["🚀 TWIN", "⚙️ FLEXI (M)", "🪑 FLEXI (Mesa)", "🧪 FÓRMULA"])
        
        def mostrar_calculos(pzas_hora):
            segundos = int(3600 / pzas_hora)
            minutos = segundos // 60
            seg_rest = segundos % 60
            tiempo_txt = f"{minutos} min {seg_rest} seg ({segundos} seg)"
            c1, c2 = st.columns(2)
            with c1: st.metric("Tiempo por Prenda", tiempo_txt)
            with c2: st.metric("Prod. por Hora", f"{pzas_hora} pzas")
            horas = [8, 10, 12]
            df = pd.DataFrame({
                "Horas": [f"{h}h" for h in horas],
                "Total": [f"{h * pzas_hora} pzas" for h in horas]
            })
            st.table(df)

        with tab1: mostrar_calculos(pzas_hora_base)
        with tab2: mostrar_calculos(pzas_hora_base + 8)
        with tab3: mostrar_calculos(pzas_hora_base - 5)
        
        with tab4:
            if seleccion in formulas:
                st.write(f"### Receta de Lavado: {seleccion}")
                df_formula = pd.DataFrame(formulas[seleccion])
                st.table(df_formula)
            else:
                st.warning("Fórmula no cargada aún. Pásale el archivo a Luis.")
            
    else:
        st.subheader(f"🧼 Detalle Lavandería: {seleccion}")
        st.info(f"📍 Área: {area} | ⚙️ Proceso: {datos[1]}")

st.sidebar.markdown("---")
st.sidebar.write(f"✅ Lavado: {seleccion}")
