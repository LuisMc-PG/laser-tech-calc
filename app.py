import streamlit as st
import pandas as pd
import math

# Configuración con el emoji del pantalón
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖", layout="wide")

# --- ESTILOS CSS REFORZADOS ---
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
    }
    button[aria-selected="true"] {
        background-color: #00ff00 !important;
        color: black !important;
    }
    .stMetric, .stDataFrame, div[data-testid="stTable"] {
        background-color: rgba(255, 255, 255, 1) !important;
        border-radius: 10px !important;
    }
    .stMetric * , .stDataFrame * , div[data-testid="stTable"] * {
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
st.caption("Ficha Técnica Digitalizada para Planta")

# --- BASE DE DATOS DE PRODUCCIÓN ---
base_datos = {
    "DELT": [40, "45%", "LÁSER"],
    "MYYA": [70, "45%", "LÁSER"],
    "BLGU": [50, "45%", "LÁSER"],
    "ZRCN": [56, "45%", "LÁSER"],
    "BFOW": [43, "45%", "LÁSER"],
    "MOBU": [43, "45%", "LÁSER"],
    "BLUV": [50, "45%", "LÁSER"],
    "RGRI": [45, "45%", "LÁSER"],
    "OVRW": [43, "45%", "LÁSER"],
    "DSP1": [43, "45%", "LÁSER"],
    "CUMB": [43, "45%", "LÁSER"],
    "ALPA": [54, "45%", "LÁSER"],
    "CTBU": [45, "45%", "LÁSER"]
}

# --- FÓRMULA DETALLADA (EXTRACCION FIEL DEL EXCEL) ---
formulas_maestras = {
    "DELT": {
        "Info": {"Tela": "ECO BLUE (NUME)", "Corte": "MN15446-2", "Prenda": "MATEO JEAN"},
        "Dry Process": [
            "1.0 BIGOTES TALLADOS (Delanteros y traseros)",
            "2.0 HAND SAND (Figura, base, manchones)",
            "3.0 LÁSER",
            "4.0 PLASTIFLECHA"
        ],
        "Lavanderia": [
            {"Paso": "4.0", "Proceso": "DESENGOME", "Condiciones": "50°C - 12 min", "Químicos": "Humectante / Amilasa"},
            {"Paso": "5.0", "Proceso": "ENJUAGUE", "Condiciones": "Frío - 4 min", "Químicos": "Agua sola"},
            {"Paso": "6.0", "Proceso": "STONE", "Condiciones": "40°C - 35 min", "Químicos": "Piedra Pómez / Enzima Abrasiva"},
            {"Paso": "10.0", "Proceso": "ENJUAGUE CALIENTE", "Condiciones": "50°C - 5 min", "Químicos": "Detergente"},
            {"Paso": "14.0", "Proceso": "SECADO", "Condiciones": "60°C - 60 min", "Químicos": "N/A"},
            {"Paso": "17.0", "Proceso": "NEUTRALIZADO", "Condiciones": "Frío - 4 min", "Químicos": "Hidroxilamina (2.0 KG)"},
            {"Paso": "19.0", "Proceso": "BAJADA DE TONO", "Condiciones": "40°C - 5 min", "Químicos": "Cloro (5.0 KG)"},
            {"Paso": "20.0", "Proceso": "NEUTRALIZADO final", "Condiciones": "Frío - 4 min", "Químicos": "Bisulfito (2.0 KG)"}
        ]
    }
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Selecciona Código de Lavado:", ["-- Selecciona --"] + opciones)

if seleccion != "-- Selecciona --":
    datos = base_datos[seleccion]
    pzas_hora_base = datos[0]
    
    st.divider()
    
    # PESTAÑAS
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 TWIN", "⚙️ FLEXI (M)", "🪑 FLEXI (Mesa)", "🧪 FÓRMULA DE LAVADO"])

    def mostrar_tiempos(pzas):
        seg = int(3600 / pzas)
        c1, c2 = st.columns(2)
        with c1: st.metric("Tiempo Unitario", f"{seg // 60}m {seg % 60}s")
        with c2: st.metric("Meta Hora", f"{pzas} pzas")
        st.table(pd.DataFrame({"Jornada": ["8h", "10h", "12h"], "Meta": [pzas*8, pzas*10, pzas*12]}))

    with tab1: mostrar_tiempos(pzas_hora_base)
    with tab2: mostrar_tiempos(pzas_hora_base + 8)
    with tab3: mostrar_tiempos(pzas_hora_base - 5)

    with tab4:
        if seleccion in formulas_maestras:
            f = formulas_maestras[seleccion]
            st.success(f"📋 FICHA TÉCNICA: {seleccion}")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**DRY PROCESS:**")
                for p in f["Dry Process"]: st.write(f"• {p}")
            with col_b:
                st.write("**DATOS TELA:**")
                st.write(f"Tela: {f['Info']['Tela']}")
                st.write(f"Prenda: {f['Info']['Prenda']}")

            st.write("---")
            st.write("**PROCESO DE LAVANDERÍA:**")
            st.table(pd.DataFrame(f["Lavanderia"]))
        else:
            st.warning("Fórmula en proceso de carga. Favor de consultar el Excel físico.")

st.sidebar.write(f"Usuario: Luis Mc")
st.sidebar.caption("UTEL - Ingeniería en Software")
