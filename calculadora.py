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
        border-top: 1px solid #30363d;
        border-right: 1px solid #30363d;
        border-bottom: 1px solid #30363d;
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

# Pestaña 4: Ficha Técnica Completa (Toda la información)
with tab4:
    st.header("🧪 Fórmula de Lavado y Procesos: DELT")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
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
        "**12. POTASIO SOPLADO:** 15 C/ÁCIDO (FIGURA, BASE, BRISEADO)",
        "**13. QUITAR PLASTIFLECHA**"
    ]
    
    for p in procesos_1:
        st.markdown(f'<div class="step-box">{p}</div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("🌊 LAVANDERÍA – SEGUNDA ETAPA")
    
    procesos_2 = [
        "**14. NEUTRALIZADO:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 4 MIN | (HIDROXILAMINA 2 KG, ANTIDHER 2 KG, SANDOCLEAN 20 KG)",
        "**15. ENJUAGUE:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 4 MIN | (AGUA SOLA)",
        "**16. BAJADA DE TONO:** NIVEL: 800 LTS | TEMP: 40 °C | TIEMPO: 5 MIN | (CLORO 5 KG)",
        "**17. NEUTRALIZADO:** NIVEL: 600 LTS | TEMP: FRIO °C | TIEMPO: 6 MIN | (BISULFITO 11 KG)",
        "**18. ENJUAGUE:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 5 MIN | (AGUA SOLA)",
        "**19. SUAVIZADO:** NIVEL: 400 LTS | TEMP: FRIO °C | TIEMPO: 3 MIN | (FINISH SOFT 5-3: 2 KG)",
        "**20. CENTRIFUGADO:** TIEMPO: 10 MIN",
        "**21. SECADO:** TIEMPO: 60 MIN | TEMP: 60 °C",
        "**22. BIGOTES PLANCHADOS:** DELANTEROS"
    ]
    
    for p in procesos_2:
        st.markdown(f'<div class="step-box">{p}</div>', unsafe_allow_html=True)

# 3. Sección de imágenes Comparativas (BMP vs Lavado)
st.write("---")
if st.checkbox("🔍 Abrir Comparativa de Diseños (BMP vs Lavado)", value=True):
    path = "./fotos/"
    
    st.subheader("📸 Comparativa Frontal")
    col1, col2 = st.columns(2)
    with col1:
        st.image(path + "DELT_frente_bmp.jpg", caption="DISEÑO LÁSER (BMP) - FRENTE", use_container_width=True)
    with col2:
        st.image(path + "DELT_frente_lavado.jpg", caption="RESULTADO FINAL - FRENTE", use_container_width=True)
    
    st.write("---")
    st.subheader("📸 Comparativa Trasera")
    col3, col4 = st.columns(2)
    with col3:
        st.image(path + "DELT_trasera_bmp.jpg", caption="DISEÑO LÁSER (BMP) - TRASERA", use_container_width=True)
    with col4:
        st.image(path + "DELT_trasera_lavado.jpg", caption="RESULTADO FINAL - TRASERA", use_container_width=True)
