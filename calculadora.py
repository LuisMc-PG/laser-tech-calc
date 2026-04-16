import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Tecnología Láser - Producción",
    page_icon="👖",
    layout="wide",
)

# Estilo visual oscuro
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    h1, h2, h3 { color: #58a6ff; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 5px 5px 0px 0px;
        padding: 10px 20px;
        color: #8b949e;
    }
    .stTabs [aria-selected="true"] { background-color: #1f6feb !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👖 Sistema de Producción Láser")

# 1. Lista desplegable para elegir el lavado
lavado_seleccionado = st.selectbox(
    "Selecciona el tipo de lavado:",
    ["DELT (Actual)", "LAVADO DE RELLENO (Prueba)"]
)

if lavado_seleccionado == "DELT (Actual)":
    st.info("**Tela:** ECO BLUE (NUME) | **Prenda:** MATEO JEAN")
    
    # Definimos los datos base del lavado DELT
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 40, "intensidad": "100 tpx"},
        "Flexi (Maniquí)": {"pzas_hora": 48, "intensidad": "80 tpx"},
        "Flexi (Mesa)": {"pzas_hora": 36, "intensidad": "68 tpx"}
    }
else:
    st.warning("Estás viendo datos de prueba.")
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 20, "intensidad": "50 tpx"},
        "Flexi (Maniquí)": {"pzas_hora": 25, "intensidad": "40 tpx"},
        "Flexi (Mesa)": {"pzas_hora": 15, "intensidad": "30 tpx"}
    }

# 2. Pestañas para separar la información por máquina
tab1, tab2, tab3 = st.tabs(["Twin (Maniquí)", "Flexi (Maniquí)", "Flexi (Mesa)"])

def mostrar_info_maquina(nombre_maquina):
    info = datos_maquinas[nombre_maquina]
    pzas_h = info["pzas_hora"]
    
    # --- Cálculos de tiempo por prenda ---
    # 3600 segundos tiene una hora
    segundos_totales = 3600 / pzas_h
    minutos = int(segundos_totales // 60)
    segundos_restantes = int(segundos_totales % 60)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pzas / Hora", f"{pzas_h} pzas")
    with col2:
        st.metric("Tiempo por Prenda", f"{minutos}m {segundos_restantes}s")
    with col3:
        st.metric("Segundos Totales", f"{int(segundos_totales)}s")

    st.write("---")
    st.subheader(f"📊 Metas de Producción - {nombre_maquina}")
    
    # Tabla de metas
    metas = {
        "Turno": ["8 Horas", "15 Horas", "24 Horas"],
        "Producción Total": [pzas_h * 8, pzas_h * 15, pzas_h * 24],
        "Intensidad": [info["intensidad"], info["intensidad"], info["intensidad"]]
    }
    st.table(metas)

with tab1:
    mostrar_info_maquina("Twin (Maniquí)")

with tab2:
    mostrar_info_maquina("Flexi (Maniquí)")

with tab3:
    mostrar_info_maquina("Flexi (Mesa)")

# --- Sección de imágenes (se mantiene al final para referencia) ---
st.write("---")
if st.checkbox("Mostrar referencias visuales"):
    col_img1, col_img2 = st.columns(2)
    path = "./fotos/"
    with col_img1:
        st.image(path + "DELT_frente_lavado.jpg", caption="Frente")
    with col_img2:
        st.image(path + "DELT_trasera_lavado.jpg", caption="Trasera")
