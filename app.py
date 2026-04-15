import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuración de la App 👖
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
    .stAlert {
        background-color: #ff4b4b !important;
        color: white !important;
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
st.caption(f"Ingeniería de Procesos | Luis Mc")

# --- BASE DE DATOS ACTUALIZADA ---
base_datos = {
    "DELT": {"pzas_base": 40, "lleva_laser": True, "intensidades": {"twin": "100tpx", "flexi_m": "90tpx", "flexi_mesa": "80tpx"}},
    "OVRW": {"pzas_base": 43, "lleva_laser": True, "intensidades": {"twin": "90tpx", "flexi_m": "70tpx", "flexi_mesa": "56tpx"}},
    "JAIL": {"pzas_base": 50, "lleva_laser": False}, # Agregado: Sin láser
    "OEDW": {"pzas_base": 30, "lleva_laser": False}  # Agregado: Sin láser
}

# --- FÓRMULAS MAESTRAS ---
formulas_maestras = {
    "JAIL": {
        "Info": {"Tela": "STRETCH DENIM", "Corte": "RELAXED", "Peso": "80 KG", "Pzas": "120 PZ"},
        "Dry Process": ["1 APLICACIÓN DE BIGOTES PLANCHADOS", "2 APLICACIÓN DE BIGOTES PLANCHADOS (SEGUNDA VUELTA)"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "SUAVIZADO", "CONDICIONES": "FRIO - 15 min", "PRODUCTO QUÍMICO": "SUAVIZANTE TEXTIL"}]
    },
    "OEDW": {
        "Info": {"Tela": "DENIM TEÑIDO", "Corte": "REGULAR", "Peso": "110 KG", "Pzas": "140 PZ"},
        "Dry Process": ["NO APLICA PROCESO EN SECO"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "TEÑIDO (OVERDYE)", "CONDICIONES": "60°C - 45 min", "PRODUCTO QUÍMICO": "COLORANTE / FIJADOR"}]
    },
    "DELT": {
        "Info": {"Tela": "ECO BLUE (NUME)", "Corte": "MN15446-2", "Peso": "100 KG", "Pzas": "169 PZ"},
        "Dry Process": ["1 BIGOTES TALLADOS", "2 HAND SAND", "3 LASER", "4 PLASTIFLECHA"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "50°C - 12 min", "PRODUCTO QUÍMICO": "HUMECTANTE"}]
    },
    "OVRW": {
        "Info": {"Tela": "ECO BLUE", "Corte": "SKINNY BASIC JEAN", "Peso": "100 KG", "Pzas": "150 PZ"},
        "Dry Process": ["1 BIGOTES DIBUJADOS", "2 HAND SAND"],
        "Lavanderia": [
            {"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "FRIO - 10 min", "PRODUCTO QUÍMICO": "ANTIDHER (1.0 KG)"},
            {"PASO": "5", "PROCESO": "ABRASIÓN", "CONDICIONES": "FRIO - 20 min", "PRODUCTO QUÍMICO": "HERZYME H CONC (150 GRS)"}
        ]
    }
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o Selecciona Código de Lavado:", ["-- Selecciona --"] + opciones)

if seleccion != "-- Selecciona --":
    config = base_datos[seleccion]
    
    # --- ALERTA DE SEGURIDAD (Si no lleva láser) ---
    if not config["lleva_laser"]:
        st.warning(f"⚠️ ATENCIÓN: El lavado {seleccion} NO incluye proceso de LÁSER. Favor de seguir la ruta manual.")
    
    st.divider()
    
    # Si lleva láser, mostramos las pestañas de metas. Si no, solo mostramos la fórmula.
    if config["lleva_laser"]:
        tab1, tab2, tab3, tab4 = st.tabs(["🚀 TWIN", "⚙️ FLEXI (M)", "🪑 FLEXI (Mesa)", "🧪 FÓRMULA"])
        
        pzas = config["pzas_base"]
        def mostrar_metas(p, i=None):
            seg = int(3600 / p)
            c1, c2, c3 = st.columns(3)
            with c1: st.metric("Tiempo Unitario", f"{seg // 60}m {seg % 60}s")
            with c2: st.metric("Meta Hora", f"{p} pzas")
            with c3: st.metric("⚡ Intensidad Láser", i if i else "N/A")

        with tab1: mostrar_metas(pzas, config["intensidades"].get("twin"))
        with tab2: mostrar_metas(pzas + 8, config["intensidades"].get("flexi_m"))
        with tab3: mostrar_metas(pzas - 5, config["intensidades"].get("flexi_mesa"))
        with tab4:
             if seleccion in formulas_maestras:
                f = formulas_maestras[seleccion]
                st.success(f"📋 FÓRMULA TÉCNICA - {seleccion}")
                st.write("**DRY PROCESS:**", f["Dry Process"])
                st.table(pd.DataFrame(f["Lavanderia"]))
    else:
        # Para lavados sin láser, vamos directo a la fórmula
        st.info("ℹ️ Este proceso es directo a Lavandería / Manual.")
        if seleccion in formulas_maestras:
            f = formulas_maestras[seleccion]
            st.success(f"📋 RUTA DE PROCESO - {seleccion}")
            st.write("**DRY PROCESS:**", f["Dry Process"])
            st.write("**LAVANDERÍA:**")
            st.table(pd.DataFrame(f["Lavanderia"]))

st.sidebar.write(f"Ingeniería de Software | Luis Mc")
