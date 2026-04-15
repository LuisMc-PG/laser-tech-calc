import streamlit as st
import pandas as pd
import math
import os

# Configuración 👖
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖", layout="wide")

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

# --- BASE DE DATOS PRODUCCIÓN ---
base_datos = {
    "DELT": [40, "45%", "LÁSER"],
    "MYYA": [70, "45%", "LÁSER"],
    "BLGU": [50, "45%", "LÁSER"],
    "ZRCN": [56, "45%", "LÁSER"],
    "BFOW": [43, "45%", "LÁSER"]
}

# --- FÓRMULA MAESTRA (CLON EXACTO DEL EXCEL) ---
formulas_maestras = {
    "DELT": {
        "Info": {"Tela": "ECO BLUE (NUME)", "Corte": "MN15446-2", "Peso": "100 KG", "Pzas": "169 PZ"},
        "Dry Process": [
            "1.0 BIGOTES TALLADOS (DIBUJADOS DELANTEROS RODILLA DELANTERA Y TRASERA)",
            "2.0 HAND SAND (FIGURA – BASE – MANCHONES)",
            "3.0 LASER",
            "4.0 PLASTIFLECHA"
        ],
        "Lavanderia": [
            {"PASO": "4.0", "PROCESO": "DESENGOME", "CONDICIONES": "50°C - 12 min", "PRODUCTO QUÍMICO": "HUMECTANTE / AMILASA"},
            {"PASO": "5.0", "PROCESO": "ENJUAGUE", "CONDICIONES": "FRIO - 4 min", "PRODUCTO QUÍMICO": "AGUA SOLA"},
            {"PASO": "6.0", "PROCESO": "STONE", "CONDICIONES": "40°C - 35 min", "PRODUCTO QUÍMICO": "ENZIMA ABRASIVA"},
            {"PASO": "10.0", "PROCESO": "ENJUAGUE CALIENTE", "CONDICIONES": "50°C - 5 min", "PRODUCTO QUÍMICO": "DETERGENTE"},
            {"PASO": "14.0", "PROCESO": "SECADO", "CONDICIONES": "60°C - 60 min", "PRODUCTO QUÍMICO": "N/A"},
            {"PASO": "17.0", "PROCESO": "NEUTRALIZADO", "CONDICIONES": "FRIO - 4 min", "PRODUCTO QUÍMICO": "HIDROXILAMINA (2.0 KG), ANTIDHER (2.0 KG), SANDOCLEAN (2.0 KG)"},
            {"PASO": "18.0", "PROCESO": "ENJUAGUE", "CONDICIONES": "FRIO - 4 min", "PRODUCTO QUÍMICO": "AGUA SOLA"},
            {"PASO": "19.0", "PROCESO": "BAJADA DE TONO", "CONDICIONES": "40.0°C - 5 min", "PRODUCTO QUÍMICO": "CLORO (5.0 KG)"},
            {"PASO": "20.0", "PROCESO": "NEUTRALIZADO", "CONDICIONES": "FRIO - 4 min", "PRODUCTO QUÍMICO": "BISULFITO (2.0 KG)"}
        ]
    }
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Selecciona Código:", ["-- Selecciona --"] + opciones)

if seleccion != "-- Selecciona --":
    pzas_hora_base = base_datos[seleccion][0]
    
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 TWIN", "⚙️ FLEXI (M)", "🪑 FLEXI (Mesa)", "🧪 FÓRMULA"])

    def mostrar_metas(pzas):
        seg = int(3600 / pzas)
        c1, c2 = st.columns(2)
        with c1: st.metric("Tiempo Unitario", f"{seg // 60}m {seg % 60}s")
        with c2: st.metric("Meta Hora", f"{pzas} pzas")
        st.table(pd.DataFrame({"Turno": ["8h", "10h", "12h"], "Meta": [pzas*8, pzas*10, pzas*12]}))

    with tab1: mostrar_metas(pzas_hora_base)
    with tab2: mostrar_metas(pzas_hora_base + 8)
    with tab3: mostrar_metas(pzas_hora_base - 5)

    with tab4:
        if seleccion in formulas_maestras:
            f = formulas_maestras[seleccion]
            st.success(f"📋 FICHA TÉCNICA: {seleccion}")
            
            # Buscador de imagen flexible por si tiene error de nombre
            archivos = os.listdir(".")
            img_final = next((a for a in archivos if a.upper().startswith(seleccion) and a.lower().endswith(('.png', '.jpg'))), None)
            if img_final: st.image(img_final, width=400)
            
            st.write("---")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**D R Y   P R O C E S S:**")
                for p in f["Dry Process"]: st.write(f"• {p}")
            with col_b:
                st.write("**DATOS TÉCNICOS:**")
                st.write(f"Tela: {f['Info']['Tela']}")
                st.write(f"Corte: {f['Info']['Corte']}")
                st.write(f"Peso: {f['Info']['Peso']}")
                st.write(f"Piezas: {f['Info']['Pzas']}")

            st.write("---")
            st.write("**L A V A N D E R Í A:**")
            st.table(pd.DataFrame(f["Lavanderia"]))
        else:
            st.warning("Fórmula no cargada. Por favor integra los datos del archivo correspondiente.")

st.sidebar.write(f"Usuario: Luis Mc")
