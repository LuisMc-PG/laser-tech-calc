import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Tecnología Láser - Calculadora",
    page_icon="👖",
    layout="wide",
)

# --- Estilo para que se vea oscuro como en tu GitHub (como el fondo negro) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stTable {
        background-color: #161b22;
        color: #c9d1d9;
        border: 1px solid #30363d;
        border-collapse: collapse;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    strong {
        color: #e6edf3;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Títulos ---
st.title("👖 Tecnología Láser - Calculadora de Producción")
st.write("---")

# --- Lavado Actual ---
st.header("🚀 Lavado Actual: DELT (Versión Actualizada)")
st.info("**Fecha:** 12/JUN/2024 | **Tela:** ECO BLUE (NUME) | **Prenda:** MATEO JEAN")

# --- Tabla de Metas de Producción (Fijas) ---
st.subheader("📊 Metas de Producción (Láser)")

# Datos para la tabla
data = {
    'Máquina': ['Twin (Maniquí)', 'Flexi (Maniquí)', 'Flexi (Mesa)'],
    'Pzas/Hora': [40, 48, 36],
    '8 hrs': [320, 384, 288],
    '15 hrs': [600, 720, 540],
    '24 hrs': [960, 1152, 864],
    'Intensidad': ['100 tpx', '80 tpx', '68 tpx']
}

# Mostrar la tabla (es automática, no es necesario hacer calculos)
st.table(data)

# --- Referencias Visuales con Imagenes de tu carpeta 'fotos' ---
st.subheader("📸 Referencias Visuales")

col1, col2 = st.columns(2)

# Ajusta las rutas si el nombre de tu carpeta es diferente (ej: 'Fotos' con F mayúscula)
path_fotos = "./fotos/" 

with col1:
    st.image(path_fotos + "DELT_frente_lavado.jpg", caption="Prenda Lavada - Frente", use_column_width=True)

with col2:
    st.image(path_fotos + "DELT_trasera_lavado.jpg", caption="Prenda Lavada - Trasera", use_column_width=True)

# --- Ficha Técnica Completa con un Expander (como el 'details') ---
with st.expander("🧪 Fórmula de Lavado y Procesos (DELT 2024)", expanded=False):
    st.write("**Información General:**")
    st.write("- **Contenido:** 77% Cotton, 13% Lyocell, 6% Polyester, 2% Elasterell, 2% Spandex")
    st.write("- **Peso:** 100 KG | **Piezas:** 169 PZAS")
    
    st.write("---")
    
    st.subheader("🛠 DRY PROCESS")
    st.write("- **Laser:** Bigotes delanteros, rodilla delantera y trasera.")
    st.write("- **Plastiflecha**")
    
    st.write("---")
    
    st.subheader("🌊 LAVANDERÍA – PRIMERA ETAPA (Lavar al derecho)")
    st.write("1. **Desengome:** 600 Lts | Frío | 8 min | (Antidher 1kg, Sandoclean 1kg, Bet 500grs, Protecther BA 500grs)")
    st.write("2. **Enjuague:** 400 Lts | Frío | 3 min")
    st.write("3. **Abrasión:** 400 Lts | Frío | 45 min")
    # ... (Puedes agregar todos los puntos aquí)
    st.write("...")
    st.write("13. **Quitar Plastiflecha**")
    
    st.write("---")
    
    st.subheader("🌊 LAVANDERÍA – SEGUNDA ETAPA")
    st.write("14. **Neutralizado:** 400 Lts | Frío | 4 min | (Hidroxilamina 2kg, Antidher 2kg, Sandoclean 20kg)")
    st.write("15. **Enjuague:** 400 Lts | Frío | 4 min")
    # ...
    st.write("...")
    st.write("22. **Bigotes Planchados:** Delanteros")
