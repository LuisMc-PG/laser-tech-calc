import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Tecnología Láser - Producción",
    page_icon="👖",
    layout="wide",
)

# Estilo visual oscuro profesional
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

# Lógica de datos según el lavado seleccionado
if lavado_seleccionado == "DELT":
    info_gral = {
        "fecha": "12/JUN/2024", "prenda": "MATEO JEAN", "tela": "ECO BLUE (NUME)",
        "peso": "100 KG", "piezas": "169 PZAS", "contenido": "77%COTTON 13%LYOCELL 6%POLYESTER 2%ELASTERELL 2%SPANDEX"
    }
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 40},
        "Flexi (Maniquí)": {"pzas_hora": 48},
        "Flexi (Mesa)": {"pzas_hora": 36}
    }
    img_prefix = "DELT"
else:
    info_gral = {
        "fecha": "15/NOV/2023", "prenda": "SKINNY BASIC JEAN", "tela": "ECO BLUE",
        "peso": "100 KG", "piezas": "150 PZAS", "contenido": "77%COTTON 13%LYOCELL 6%POLYESTER 2%ELASTERELL 2%SPANDEX"
    }
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 50},
        "Flexi (Maniquí)": {"pzas_hora": 58},
        "Flexi (Mesa)": {"pzas_hora": 50}
    }
    img_prefix = "OVRW"

st.info(f"**PROCESANDO:** {lavado_seleccionado} | **PRENDA:** {info_gral['prenda']} | **TELA:** {info_gral['tela']}")

# 2. Pestañas de Máquinas
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
    st.header(f"🧪 Fórmula Detallada: {lavado_seleccionado}")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"**INFO GENERAL**\n* **FECHA:** {info_gral['fecha']}\n* **CONTENIDO:** {info_gral['contenido']}\n* **PESO:** {info_gral['peso']}\n* **PIEZAS:** {info_gral['piezas']}")
    
    if lavado_seleccionado == "DELT":
        with col_b: st.markdown("**DRY PROCESS**\n* LASER: BIGOTES, RODILLA\n* PLASTIFLECHA")
        st.subheader("🌊 PROCESO DE LAVANDERÍA")
        pasos = [
            "1. DESENGOME: 600 LTS | FRIO | 8 MIN | ANTIDHER 1 KG, SANDOCLEAN 1 KG, BET 500 GRS, PROTECTHER BA 500 GRS",
            "2. ENJUAGUE: 400 LTS | FRIO | 3 MIN | AGUA SOLA",
            "3. ABRASION: 400 LTS | FRIO | 45 MIN | ANTIDHER 2 KG, SANDOCLEAN 2 KG, H CON 600 GRS, PROTECTHER BA 600 GRS",
            "4. ENJUAGUE: 600 LTS | FRIO | 3 MIN",
            "5. ENJUAGUE: 600 LTS | FRIO | 3 MIN",
            "6. BAJADA DE TONO: 800 LTS | 40 °C | 23 MIN | CLORO 40",
            "7. ENJUAGUE: 400 LTS | FRIO | 1 MIN",
            "8. NEUTRALIZADO: 600 LTS | FRIO | 8 MIN",
            "9. ENJUAGUE: 500 LTS | FRIO | 4 MIN",
            "10. CENTRIFUGADO: 10 MIN",
            "11. SECADO: 60 MIN | 60 °C",
            "12. POTASIO SOPLADO: 15 C/ÁCIDO",
            "13. QUITAR PLASTIFLECHA",
            "14. SEGUNDA ETAPA - NEUTRALIZADO: 400 LTS | 4 MIN",
            "15. BAJADA DE TONO: 800 LTS | 40 °C | 5 MIN | CLORO 5 KG",
            "16. NEUTRALIZADO: 600 LTS | 6 MIN | BISULFITO 11 KG",
            "17. SUAVIZADO: 400 LTS | 3 MIN | FINISH SOFT 2 KG",
            "18. SECADO FINAL: 60 MIN | 60 °C",
            "19. BIGOTES PLANCHADOS"
        ]
    else:
        with col_b: st.markdown("**DRY PROCESS**\n* BIGOTES DIBUJADOS DELANTEROS – CHEVRONS\n* HAND SAND FIGURA – BASE – MANCHON\n* DESTROY")
        st.subheader("🌊 PROCESO DE LAVANDERÍA (ETAPA 1)")
        pasos = [
            "1. DESENGOME: 600 LTS | FRIO | 10 MIN | ANTIDHER 1 KG, SANDOCLEAN 1 KG, ALFADHER 300 GRS, PROTECTHER BA 500 GRS",
            "2. ENJUAGUE: 400 LTS | FRIO | 3 MIN | AGUA SOLA",
            "3. ABRASION: 300 LTS | FRIO | 60 MIN | HERZYME 400 GRS, ANTIDHER 1.2 KG, SANDOCLEAN 1.2 KG, PROTECTHER BA 500 GRS",
            "4. ENJUAGUE: 600 LTS | FRIO | 3 MIN | ANTIDHER 600 GRS, SANDOCLEAN 600 GRS",
            "5. ENJUAGUE: 600 LTS | FRIO | 3 MIN | AGUA SOLA",
            "6. ENJUAGUE: 600 LTS | FRIO | 3 MIN | AGUA SOLA",
            "7. ENJUAGUE: 600 LTS | FRIO | 3 MIN | ALCAPER 500 GRS",
            "8. ENJUAGUE: 600 LTS | FRIO | 3 MIN | AGUA SOLA",
            "9. CENTRIFUGADO: 8 MIN",
            "10. SECADO: 60 MIN | 60 °C",
            "11. SOPLAR SKY: FIGURA – BASE – MANCHÓN | NEARBLEACH 350 GRS, CATALINE SKY 75 GRS, PEROXIDO 75 GRS",
            "**--- SEGUNDA ETAPA (CURAR EN SECADORA 90ºC 30 MIN) ---**",
            "12. NEUTRALIZADO: 600 LTS | FRIO | 5 MIN | HIDROXILAMINA 2 KG",
            "13. ENJUAGUE: 400 LTS | 30 °C | 3 MIN",
            "14. ABRASION: 200 LTS | 30 °C | 20 MIN | HERZYME 150 GRS, ANTIDHER 1 KG, SANDOCLEAN 1 KG, PROTECTHER BA 300 GRS",
            "15. ENJUAGUE: 400 LTS | FRIO | 3 MIN",
            "16. ENJUAGUE: 400 LTS | FRIO | 9 MIN | HERTREX 500 GRS",
            "17. ENJUAGUE: 400 LTS | FRIO | 3 MIN",
            "18. SUAVIZADO: 400 LTS | FRIO | 3 MIN | FINISH SOFT 2 KG",
            "19. CENTRIFUGADO: 8 MIN",
            "20. SECADO: 60 MIN | 60 °C",
            "21. BIGOTES PLANCHADOS - DELANTEROS"
        ]
    
    for p in pasos:
        st.markdown(f'<div class="step-box">{p}</div>', unsafe_allow_html=True)

# 3. Comparativa de Fotos Dinámica (BMP vs Lavado)
st.write("---")
if st.checkbox("🔍 Ver Comparativa Completa (BMP vs Lavado)", value=True):
    path = "./fotos/"
    
    st.subheader(f"📸 VISTA FRONTAL - {lavado_seleccionado}")
    col1, col2 = st.columns(2)
    with col1: 
        st.image(f"{path}{img_prefix}_frente_bmp.jpg", caption="DISEÑO (BMP)", use_container_width=True)
    with col2: 
        st.image(f"{path}{img_prefix}_frente_lavado.jpg", caption="LAVADO FINAL", use_container_width=True)
    
    st.write("---")
    st.subheader(f"📸 VISTA TRASERA - {lavado_seleccionado}")
    col3, col4 = st.columns(2)
    with col3: 
        st.image(f"{path}{img_prefix}_trasera_bmp.jpg", caption="DISEÑO (BMP)", use_container_width=True)
    with col4: 
        st.image(f"{path}{img_prefix}_trasera_lavado.jpg", caption="LAVADO FINAL", use_container_width=True)
