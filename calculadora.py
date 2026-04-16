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
    .step-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #58a6ff;
        margin-bottom: 10px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👖 Sistema de Producción Láser")

# 1. Selección de Lavado
lavado_seleccionado = st.selectbox(
    "Selecciona el tipo de lavado:",
    ["DELT", "OVRW"]
)

# Lógica de datos según el lavado
if lavado_seleccionado == "DELT":
    info_gral = {
        "fecha": "12/JUN/2024", "prenda": "MATEO JEAN", "tela": "ECO BLUE (NUME)",
        "peso": "100 KG", "piezas": "169 PZAS", "contenido": "77%COTTON 13%LYOCELL 6%POLYESTER 2%ELASTERELL 2%SPANDEX"
    }
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 40, "intensidad": "100 tpx"},
        "Flexi (Maniquí)": {"pzas_hora": 48, "intensidad": "80 tpx"},
        "Flexi (Mesa)": {"pzas_hora": 36, "intensidad": "68 tpx"}
    }
    img_prefix = "DELT"
else:
    info_gral = {
        "fecha": "15/NOV/2023", "prenda": "SKINNY BASIC JEAN", "tela": "ECO BLUE",
        "peso": "100 KG", "piezas": "150 PZAS", "contenido": "77%COTTON 13%LYOCELL 6%POLYESTER 2%ELASTERELL 2%SPANDEX"
    }
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 50, "intensidad": "Intensidad OVRW"},
        "Flexi (Maniquí)": {"pzas_hora": 58, "intensidad": "Intensidad OVRW"},
        "Flexi (Mesa)": {"pzas_hora": 50, "intensidad": "Intensidad OVRW"}
    }
    img_prefix = "OVRW"

st.info(f"**FECHA:** {info_gral['fecha']} | **TELA:** {info_gral['tela']} | **PRENDA:** {info_gral['prenda']}")

# 2. Pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Twin (Maniquí)", "Flexi (Maniquí)", "Flexi (Mesa)", "🧪 Ficha Técnica"])

def mostrar_info_maquina(nombre_maquina):
    info = datos_maquinas[nombre_maquina]
    pzas_h = info["pzas_hora"]
    segundos_totales = 3600 / pzas_h
    minutos = int(segundos_totales // 60)
    segundos_restantes = int(segundos_totales % 60)
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Pzas / Hora", f"{pzas_h} pzas")
    with col2: st.metric("Tiempo por Prenda", f"{minutos}m {segundos_restantes}s")
    with col3: st.metric("Segundos Totales", f"{int(segundos_totales)}s")
    
    st.write("---")
    st.subheader(f"📊 Metas de Producción - {nombre_maquina}")
    metas = {
        "Turno": ["8 Horas", "15 Horas", "24 Horas"],
        "Producción Total": [pzas_h * 8, pzas_h * 15, pzas_h * 24]
    }
    st.table(metas)

with tab1: mostrar_info_maquina("Twin (Maniquí)")
with tab2: mostrar_info_maquina("Flexi (Maniquí)")
with tab3: mostrar_info_maquina("Flexi (Mesa)")

# Pestaña 4: Ficha Técnica Dinámica
with tab4:
    st.header(f"🧪 Fórmula de Lavado: {lavado_seleccionado}")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"**INFO GENERAL**\n* **CONTENIDO:** {info_gral['contenido']}\n* **PESO:** {info_gral['peso']}\n* **PIEZAS:** {info_gral['piezas']}")
    
    if lavado_seleccionado == "DELT":
        with col_b: st.markdown("**DRY PROCESS**\n* LASER: BIGOTES, RODILLA\n* PLASTIFLECHA")
        st.subheader("🌊 PROCESO DE LAVANDERÍA")
        pasos = ["1. DESENGOME: 600 LTS / 8 MIN", "2. ABRASION: 400 LTS / 45 MIN"] # (Aquí va tu lista larga anterior)
    else:
        with col_b: st.markdown("**DRY PROCESS**\n* BIGOTES DIBUJADOS\n* HAND SAND FIGURA\n* DESTROY")
        st.subheader("🌊 PROCESO DE LAVANDERÍA (ETAPA 1)")
        pasos_ovrw = [
            "**1. DESENGOME:** 600 LTS | FRIO | 10 MIN | ANTIDHER 1 KG, SANDOCLEAN 1 KG, ALFADHER 300 GRS, PROTECTHER BA 500 GRS",
            "**2. ENJUAGUE:** 400 LTS | FRIO | 3 MIN | AGUA SOLA",
            "**3. ABRASION:** 300 LTS | FRIO | 60 MIN | HERZYME 400 GRS, ANTIDHER 1.2 KG, SANDOCLEAN 1.2 KG",
            # ... se agregarán todos los demás pasos en el siguiente paso
        ]
        for p in pasos_ovrw: st.markdown(f'<div class="step-box">{p}</div>', unsafe_allow_html=True)

# 3. Comparativa de Fotos Dinámica
st.write("---")
if st.checkbox("🔍 Ver Comparativa (BMP vs Lavado)", value=True):
    path = "./fotos/"
    col1, col2 = st.columns(2)
    with col1: st.image(f"{path}{img_prefix}_frente_bmp.jpg", caption=f"BMP FRENTE {lavado_seleccionado}", use_container_width=True)
    with col2: st.image(f"{path}{img_prefix}_frente_lavado.jpg", caption=f"LAVADO FRENTE {lavado_seleccionado}", use_container_width=True)
