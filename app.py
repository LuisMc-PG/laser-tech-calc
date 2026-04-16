import streamlit as st
import pandas as pd
import os
from PIL import Image

# 1. Configuración de la App 👖
st.set_page_config(page_title="Sistema Control Textil", page_icon="👖", layout="wide")

# 2. --- ESTILOS CSS (La "piel" de la aplicación) ---
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

# 3. --- BASE DE DATOS MAESTRA ---
base_datos = {
    "DELT": {"pzas_base": 40, "lleva_laser": True, "intensidades": {"twin": "100tpx", "flexi_m": "90tpx", "flexi_mesa": "80tpx"}},
    "OVRW": {"pzas_base": 43, "lleva_laser": True, "intensidades": {"twin": "90tpx", "flexi_m": "70tpx", "flexi_mesa": "56tpx"}},
    "JAIL": {"pzas_base": 50, "lleva_laser": False},
    "OEDW": {"pzas_base": 30, "lleva_laser": False}
}

# --- FÓRMULAS TÉCNICAS ---
formulas_maestras = {
    "DELT": {
        "Info": {"Tela": "ECO BLUE (NUME)", "Corte": "MN15446-2", "Peso": "100 KG", "Pzas": "169 PZ"},
        "Dry Process": ["1 BIGOTES TALLADOS", "2 HAND SAND", "3 LASER", "4 PLASTIFLECHA"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "50°C - 12 min", "PRODUCTO QUÍMICO": "HUMECTANTE / AMILASA"}]
    },
    "OVRW": {
        "Info": {"Tela": "ECO BLUE", "Corte": "SKINNY BASIC JEAN", "Peso": "100 KG", "Pzas": "150 PZ"},
        "Dry Process": ["1 BIGOTES (CHEVRONS)", "2 HAND SAND (FIGURA-BASE-MANCHON)"],
        "Lavanderia": [
            {"PASO": "1", "PROCESO": "DESENGOME", "CONDICIONES": "FRIO - 10 min", "PRODUCTO QUÍMICO": "ANTIDHER (1.0 KG) / SANDOCLEAN (1.0 KG) / ALFADHER (300 GRS)"},
            {"PASO": "2", "PROCESO": "SOPLAR SKY", "CONDICIONES": "MANUAL", "PRODUCTO QUÍMICO": "NEARBLEACH (350 GRS) / CATALINE SKY (75 GRS) / PEROXIDO (75 GRS)"},
            {"PASO": "3", "PROCESO": "NEUTRALIZADO", "CONDICIONES": "FRIO - 5 min", "PRODUCTO QUÍMICO": "HIDROXILAMINA (2.0 KG)"},
            {"PASO": "4", "PROCESO": "ENJUAGUE", "CONDICIONES": "30°C - 3 min", "PRODUCTO QUÍMICO": "AGUA SOLA"},
            {"PASO": "5", "PROCESO": "ABRASIÓN", "CONDICIONES": "FRIO - 20 min", "PRODUCTO QUÍMICO": "HERZYME H CONC (150 GRS) / ANTIDHER (1.0 KG) / SANDOCLEAN (1.0 KG)"},
            {"PASO": "6", "PROCESO": "ENJUAGUE", "CONDICIONES": "FRIO - 3 min", "PRODUCTO QUÍMICO": "AGUA SOLA"}
        ]
    },
    "JAIL": {
        "Info": {"Tela": "STRETCH", "Corte": "RELAXED", "Peso": "80 KG", "Pzas": "120 PZ"},
        "Dry Process": ["1 APLICACIÓN DE BIGOTES PLANCHADOS", "2 APLICACIÓN DE BIGOTES PLANCHADOS (2DA)"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "SUAVIZADO", "CONDICIONES": "FRIO - 15 min", "PRODUCTO QUÍMICO": "SUAVIZANTE"}]
    },
    "OEDW": {
        "Info": {"Tela": "TEÑIDO", "Corte": "REGULAR", "Peso": "110 KG", "Pzas": "140 PZ"},
        "Dry Process": ["NO APLICA LÁSER"],
        "Lavanderia": [{"PASO": "1", "PROCESO": "OVERDYE", "CONDICIONES": "60°C", "PRODUCTO QUÍMICO": "COLORANTE"}]
    }
}

# 4. --- FUNCIONES DE APOYO ---
def mostrar_imagen_optimizada(nombre_base, es_bmp=False):
    img_path = None
    for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG']:
        if os.path.exists(nombre_base + ext):
            img_path = nombre_base + ext
            break
    if img_path:
        try:
            image = Image.open(img_path)
            if not es_bmp:
                width, height = image.size
                if width > height:
                    image = image.rotate(-90, expand=True)
            st.image(image, use_container_width=True)
        except: 
            st.error("Error al cargar imagen")
    else: 
        st.info(f"Pendiente de subir imagen para: {nombre_base}")

def calcular_metas_tabla(pzas_hora):
    df_metas = pd.DataFrame({
        "Turno": ["8 Horas", "10 Horas", "12 Horas", "24 Horas"],
        "Meta Total (Pzas)": [pzas_hora*8, pzas_hora*10, pzas_hora*12, pzas_hora*24]
    })
    st.table(df_metas)

# 5. --- INTERFAZ PRINCIPAL (Donde estaba el error) ---
opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o Selecciona Código de Lavado:", opciones)

# Creación de Pestañas
tab1, tab2, tab3 = st.tabs(["📊 Métricas de Producción", "🧪 Receta / Fórmula", "📸 Diseño Visual"])

with tab1:
    st.header(f"Producción - {seleccion}")
    pzas_h = base_datos[seleccion]["pzas_base"]
    
    col_metrica, col_laser = st.columns(2)
    with col_metrica:
        st.metric("Capacidad Base", f"{pzas_h} Pzas/Hora")
    with col_laser:
        lleva = "SÍ ✅" if base_datos[seleccion]["lleva_laser"] else "NO ❌"
        st.metric("Proceso Láser", lleva)
    
    st.subheader("Planificación de Metas")
    calcular_metas_tabla(pzas_h)

with tab2:
    st.header("Instrucciones de Lavandería")
    datos_formula = formulas_maestras[seleccion]
    
    # Mostrar Info General
    st.markdown("### 📋 Datos del Lote")
    info = datos_formula["Info"]
    c1, c2, c3, c4 = st.columns(4)
    c1.write(f"**Tela:** \n{info['Tela']}")
    c2.write(f"**Corte:** \n{info['Corte']}")
    c3.write(f"**Peso:** \n{info['Peso']}")
    c4.write(f"**Cant:** \n{info['Pzas']}")
    
    st.divider()
    
    # Procesos
    st.markdown("### 🧼 Pasos de Lavado")
    df_lavado = pd.DataFrame(datos_formula["Lavanderia"])
    st.table(df_lavado)
    
    st.markdown("### 🛠 Dry Process (Acabados)")
    for proceso in datos_formula["Dry Process"]:
        st.write(f"- {proceso}")

with tab3:
    st.header("Referencia de Diseño")
    st.write(f"Mostrando archivos relacionados con el código: **{seleccion}**")
    mostrar_imagen_optimizada(seleccion)
