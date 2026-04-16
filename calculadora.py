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
        background-color: #0d1117;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #58a6ff;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👖 Sistema de Producción Láser")

# 1. Selección de Lavado
lavado_seleccionado = st.selectbox(
    "Selecciona el tipo de lavado:",
    ["DELT (Actual)", "LAVADO DE RELLENO (Prueba)"]
)

if lavado_seleccionado == "DELT (Actual)":
    st.info("**FECHA:** 12/JUN/2024 | **TELA:** ECO BLUE (NUME) | **PRENDA:** MATEO JEAN")
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 40, "intensidad": "100 tpx"},
        "Flexi (Maniquí)": {"pzas_hora": 48, "intensidad": "80 tpx"},
        "Flexi (Mesa)": {"pzas_hora": 36, "intensidad": "68 tpx"}
    }
else:
    st.warning("Datos de prueba.")
    datos_maquinas = {
        "Twin (Maniquí)": {"pzas_hora": 20, "intensidad": "50 tpx"},
        "Flexi (Maniquí)": {"pzas_hora": 25, "intensidad": "40 tpx"},
        "Flexi (Mesa)": {"pzas_hora": 15, "intensidad": "30 tpx"}
    }

# 2. Pestañas de navegación
tab1, tab2, tab3, tab4 = st.tabs(["Twin (Maniquí)", "Flexi (Maniquí)", "Flexi (Mesa)", "🧪 Ficha Técnica de Lavado"])

def mostrar_info_maquina(nombre_maquina):
    info = datos_maquinas[nombre_maquina]
    pzas_h = info["pzas_hora"]
    
    # Cálculos de tiempo por prenda
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
    metas = {
        "Turno": ["8 Horas", "15 Horas", "24 Horas"],
        "Producción Total": [pzas_h * 8, pzas_h * 15, pzas_h * 24],
        "Intensidad": [info["intensidad"], info["intensidad"], info["intensidad"]]
    }
    st.table(metas)

# Contenido de las pestañas de máquinas
with tab1: mostrar_info_maquina("Twin (Maniquí)")
with tab2: mostrar_info_maquina("Flexi (Maniquí)")
with tab3: mostrar_info_maquina("Flexi (Mesa)")

# Pestaña 4: Ficha Técnica Completa (Sin Resúmenes)
with tab4:
    st.header("🧪 Fórmula de Lavado y Procesos: DELT")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **INFORMACIÓN GENERAL**
        * **CONTENIDO:** 77% COTTON 13% LYOCELL 6% POLYESTER 2% ELASTERELL 2% SPANDEX
        * **PESO:** 100 KG
        * **PIEZAS:** 169 PZAS
        """)
    with col_b:
        st.markdown("""
        **DRY PROCESS**
        * **LASER:** BIGOTES DELANTEROS, RODILLA DELANTERA Y TRASERA
        * **PLASTIFLECHA**
        """)

    st.write("---")
    
    st.subheader("🌊 LAVANDERÍA – PRIMERA ETAPA (LAVAR AL DERECHO)")
    
    procesos_1 = [
        "**1. DESENGOME:** NIVEL: 600 LTS | TEMP: FRIO °C | TIEMPO: 8 MIN | (ANTIDHER 1 KG, SANDOCLEAN 1 KG, BET 500 GRS, PROTECTHER BA 500 GRS)",
        "**2. ENJUAGUE:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 3 MIN | (AGUA SOLA)",
        "**3. ABRASION:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 45 MIN | (ANTIDHER 2 KG, SANDOCLEAN 2 KG, H CON 600 GRS, PROTECTHER BA 600 GRS)",
        "**4. ENJUAGUE:** NIVEL: 600 LTS | TEMP: FRIO °C | TIEMPO: 3 MIN | (AGUA SOLA)",
        "**5. ENJUAGUE:** NIVEL: 600 LTS | TEMP: FRIO °C | TIEMPO: 3 MIN | (AGUA SOLA)",
        "**6. BAJADA DE TONO:** NIVEL: 800 LTS | TEMP: 40 °C | TIEMPO: 23 MIN | (PROTECTHER BA 500 GRS, CLORO 40)",
        "**7. ENJUAGUE:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 1 MIN | (AGUA SOLA)",
        "**8. NEUTRALIZADO:** NIVEL: 600 LTS | TEMP: FRIO °C | TIEMPO: 8 MIN",
        "**9. ENJUAGUE:** NIVEL: 500 LTS | TEMP: FRIO °C | TIEMPO: 4 MIN | (AGUA SOLA)",
        "**10. CENTRIFUGADO:** TIEMPO: 10 MIN",
        "**11. SECADO:** TIEMPO: 60 MIN | TEMP: 60 °C",
        "**12. POTASIO SOPLADO:** 15 C/ÁC
