import streamlit as st
import pandas as pd
import math

# Configuración de página con nuevo icono de precisión (target)
st.set_page_config(page_title="Sistema Control Textil", page_icon="🎯")

# --- ESTILOS CSS MEJORADOS PARA LEGIBILIDAD TOTAL ---
st.markdown(
    """
    <style>
    /* Fondo de textura de mezclilla para toda la app */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/denim.png");
        background-color: #1a4175; /* Color azul base de mezclilla */
        background-attachment: fixed;
    }

    /* --- SOLUCIÓN DE CONTRASTE --- */
    /* Forzar color BLANCO con contorno NEGRO sutil para TODO el texto */
    html, body, [data-testid="stWidgetLabel"], .stSelectbox label, p, div, span, h1, h2, h3, h4, h5, h6 {
        color: white !important;
        text-shadow: 
            -1px -1px 0 #000,  
             1px -1px 0 #000,
            -1px  1px 0 #000,
             1px  1px 0 #000 !important; /* Contorno negro para legibilidad */
    }

    /* Fondo blanco semi-transparente para las tablas y métricas (mantener contraste interno) */
    .stMetric, .stDataFrame, div[data-testid="stTable"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Reajustar texto DENTRO de métricas y tablas para que sea oscuro */
    .stMetric div, .stDataFrame div, div[data-testid="stTable"] div {
        color: #1a4175 !important;
        text-shadow: none !important; /* Quitar contorno dentro de fondos claros */
    }
    
    /* Estilo para el título principal con efecto neón láser verde */
    .laser-title {
        color: #00ff00; /* Verde láser */
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO CON EFECTO LÁSER Y NUEVO EMOJI 🎯 ---
st.markdown('<h1 class="laser-title">🎯 Sistema de Gestión de Lavados</h1>', unsafe_allow_html=True)
st.markdown("### Desarrollado por: **Luis Mc**")

# --- BASE DE DATOS MAESTRA ---
# Formato: "CÓDIGO": [Segundos, "Intensidad o Proceso", "Área"]
base_datos = {
    # ÁREA: LÁSER
    "MYYA": [51, "45%", "LÁSER"],
    "BLGU": [72, "45%", "LÁSER"],
    "ZRCN": [64, "45%", "LÁSER"],
    "BFOW": [84, "45%", "LÁSER"],
    "DELT": [90, "45%", "LÁSER"],
    "MOBU": [84, "45%", "LÁSER"],
    "BLUV": [72, "45%", "LÁSER"],
    "RGRI": [80, "45%", "LÁSER"],
    "OVRW": [84, "45%", "LÁSER"],
    "DSP1": [84, "45%", "LÁSER"],
    "CUMB": [84, "45%", "LÁSER"],
    "ALPA": [67, "45%", "LÁSER"],
    "CTBU": [80, "45%", "LÁSER"],
    
    # ÁREA: LAVANDERÍA / OTROS
    "JAIL": [0, "SUAVIZADO", "LAVANDERÍA"],
    "OEDW": [0, "TEÑIDO", "LAVANDERÍA"],
    "STONE": [0, "DESLAVE", "LAVANDERÍA"]
}

# --- INTERFAZ DEL JEFE ---

# Lista desplegable automática
opciones = sorted(list(base_datos.keys()))
seleccion = st.selectbox("Busca o selecciona un código:", ["-- Selecciona un lavado --"] + opciones)

if seleccion != "-- Selecciona un lavado --":
    datos = base_datos[seleccion]
    segundos_totales = datos[0]
    info_extra = datos[1]
    area = datos[2]
    
    st.divider()
    
    if area == "LÁSER":
        st.subheader(f"🎯 Información de Láser: {seleccion}")
        
        # Formato de tiempo (Minutos y Segundos)
        minutos = segundos_totales // 60
        segundos_rest = segundos_totales % 60
        tiempo_texto = f"{minutos} min {segundos_rest} seg ({segundos_totales} seg)"
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tiempo de Marcado", tiempo_texto)
        with col2:
            st.metric("Intensidad", info_extra)
            
        # Tabla de producción automática
        st.markdown("#### 🕒 Producción Estimada")
        horas = [8, 10, 12, 24]
        produccion = [math.floor((h * 3600) / segundos_totales) for h in horas]
        
        df = pd.DataFrame({
            "Turno": [f"{h} Horas" for h in horas],
            "Capacidad": [f"{p} prendas" for p in produccion]
        })
        st.table(df)
        
    else:
        # Si es un proceso de Lavandería
        st.subheader(f"🧼 Información de Lavandería: {seleccion}")
        # Alerta amarilla legible gracias al CSS
        st.warning(f"Este código pertenece al área de **{area}**")
        st.info(f"⚙️ **Proceso requerido:** {info_extra}")
        st.caption("Nota: Este proceso no se realiza en las máquinas láser.")

# Pie de página profesional
st.sidebar.markdown("---")
st.sidebar.write("✅ **Base de datos actualizada**")
st.sidebar.write(f"Total de códigos: {len(base_datos)}")
