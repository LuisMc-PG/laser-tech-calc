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
    div[data-baseweb="select"], div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #000000 !important;
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
st.caption(f"Ingeniería de Procesos | Luis Mc")

# --- BASE DE DATOS DE PRODUCCIÓN ---
base_datos = {
    "DELT": {
        "pzas_base": 40,
        "intensidades": {"twin": "100tpx", "flexi_m": "90tpx", "flexi_mesa": "80tpx"}
    },
    "OVRW": {
        "pzas_base": 43,
        "intensidades": {"twin": "90tpx", "flexi_m": "70tpx", "flexi_mesa": "56tpx"}
    }
}

# --- FÓRMULAS MAESTRAS (Actualizada con cantidades exactas) ---
formulas_maestras = {
    "DELT": {
        "Info": {"Tela": "ECO BLUE (NUME)", "Corte": "MN15446-2", "Peso": "100 KG", "Pzas": "169 PZ"},
        "Dry Process": ["1 BIGOTES TALLADOS", "2 HAND SAND", "3 LASER", "4 PLASTIFLECHA"],
        "Lavanderia": [
            {"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "50°C - 12 min", "PRODUCTO QUÍMICO": "HUMECTANTE / AMILASA"}
        ]
    },
    "OVRW": {
        "Info": {"Tela": "ECO BLUE", "Corte": "SKINNY BASIC JEAN", "Peso": "100 KG", "Pzas": "150 PZ"},
        "Dry Process": [
            "1 BIGOTES (DIBUJADOS DELANTEROS – CHEVRONS)",
            "2 HAND SAND (FIGURA – BASE – MANCHON)"
        ],
        "Lavanderia": [
            {"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "FRIO - 10 min", "PRODUCTO QUÍMICO": "ANTIDHER (1.0 KG) / SANDOCLEAN (1.0 KG) / ALFADHER (300 GRS)"},
            {"PASO": "2", "PROCESO": "SOPLAR SKY", "CONDICIONES": "FIGURA-BASE-MANCHON", "PRODUCTO QUÍMICO": "NEARBLEACH (350 GRS) / CATALINE SKY (75 GRS) / PEROXIDO (75 GRS)"},
            {"PASO": "3", "PROCESO": "NEUTRALIZADO", "CONDICIONES": "FRIO - 5 min", "PRODUCTO QUÍMICO": "HIDROXILAMINA (2.0 KG)"},
            {"PASO": "4", "PROCESO": "ENJUAGUE", "CONDICIONES": "30°C - 3 min", "PRODUCTO QUÍMICO": "AGUA SOLA"},
            {"PASO": "5", "PROCESO": "ABRASIÓN", "CONDICIONES": "FRIO - 20 min", "PRODUCTO QUÍMICO": "HERZYME H CONC (150 GRS) / ANTIDHER (1.0 KG) / SANDOCLEAN (1.0 KG) / PROTECTHER BA (300 GRS)"},
            {"PASO": "6", "PROCESO": "ENJUAGUE", "CONDICIONES": "FRIO - 3 min", "PRODUCTO QUÍMICO": "AGUA SOLA"}
        ]
    }
}

opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Selecciona Código de Lavado:", ["-- Selecciona --"] + opciones)

if seleccion != "-- Selecciona --":
    config = base_datos[seleccion]
    pzas_hora_base = config["pzas_base"]
    
    st.divider()
    
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 TWIN", "⚙️ FLEXI (M)", "🪑 FLEXI (Mesa)", "🧪 FÓRMULA"])

    def mostrar_metas(pzas, intensidad=None):
        seg = int(3600 / pzas)
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Tiempo Unitario", f"{seg // 60}m {seg % 60}s")
        with c2: st.metric("Meta Hora", f"{pzas} pzas")
        with c3: st.metric("⚡ Intensidad Láser", intensidad if intensidad else "N/D")
        st.table(pd.DataFrame({"Turno": ["8h", "10h", "12h"], "Meta Total": [pzas*8, pzas*10, pzas*12]}))

    with tab1: mostrar_metas(pzas_hora_base, config.get("intensidades", {}).get("twin"))
    with tab2: mostrar_metas(pzas_hora_base + 8, config.get("intensidades", {}).get("flexi_m"))
    with tab3: mostrar_metas(pzas_hora_base - 5, config.get("intensidades", {}).get("flexi_mesa"))

    with tab4:
        if seleccion in formulas_maestras:
            f = formulas_maestras[seleccion]
            st.success(f"📋 VISUALIZACIÓN Y CONTRASTE: PATRÓN DE DISEÑO VS. ACABADO TEXTIL - {seleccion}")
            
            def buscar_y_rotar_img(nombre_base):
                img_path = None
                for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG']:
                    if os.path.exists(nombre_base + ext):
                        img_path = nombre_base + ext
                        break
                if img_path:
                    try:
                        image = Image.open(img_path)
                        width, height = image.size
                        if width > height:
                            image = image.rotate(-90, expand=True)
                        return image
                    except: return None
                return None

            # --- COMPARATIVA FRONTAL ---
            st.subheader("🖼️ ANÁLISIS DE PATRÓN FRONTAL")
            col1, col2 = st.columns(2)
            with col1:
                img_path = None
                for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG']:
                    if os.path.exists(f"{seleccion}_frente_bmp" + ext):
                        img_path = f"{seleccion}_frente_bmp" + ext
                        break
                if img_path: st.image(img_path, caption="Patrón Digital (Frente)", use_container_width=True)
                else: st.info(f"Pendiente: {seleccion}_frente_bmp.png")
            with col2:
                img_lavado = buscar_y_rotar_img(f"{seleccion}_frente_lavado")
                if img_lavado: st.image(img_lavado, caption="Resultado Post-Lavado (Frente)", use_container_width=True)
                else: st.info(f"Pendiente: {seleccion}_frente_lavado.png")

            st.divider()

            # --- COMPARATIVA TRASERA ---
            st.subheader("🖼️ ANÁLISIS DE PATRÓN TRASERO")
            col3, col4 = st.columns(2)
            with col3:
                img_path_t = None
                for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG']:
                    if os.path.exists(f"{seleccion}_trasera_bmp" + ext):
                        img_path_t = f"{seleccion}_trasera_bmp" + ext
                        break
                if img_path_t: st.image(img_path_t, caption="Patrón Digital (Trasera)", use_container_width=True)
                else: st.info(f"Pendiente: {seleccion}_trasera_bmp.png")
            with col4:
                img_lavado_t = buscar_y_rotar_img(f"{seleccion}_trasera_lavado")
                if img_lavado_t: st.image(img_lavado_t, caption="Resultado Post-Lavado (Trasera)", use_container_width=True)
                else: st.info(f"Pendiente: {seleccion}_trasera_lavado.png")
            
            st.divider()
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**D R Y   P R O C E S S:**")
                for p in f["Dry Process"]: st.write(f"• {p}")
            with col_b:
                st.write("**DATOS TÉCNICOS:**")
                st.write(f"Tela: {f['Info']['Tela']}")
                st.write(f"Prenda: {f['Info']['Corte']}")
                st.write(f"Carga: {f['Info']['Peso']} / {f['Info']['Pzas']}")

            st.write("**L A V A N D E R Í A:**")
            st.table(pd.DataFrame(f["Lavanderia"]))

st.sidebar.write(f"Ingeniería de Software | Luis Mc")
