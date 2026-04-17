import streamlit as st
import pandas as pd

st.title("👖 Sistema de Producción Láser")

# 1. EL ARCHIVERO (Diccionario)
datos_lavados = {
    "DELT": {
        "Twin": {"velocidad": 40, "intensidad": "90 tpx"},
        "Flexi-Maniquí": {"velocidad": 46, "intensidad": "70 tpx"},
        "Flexi-Mesa": {"velocidad": 35, "intensidad": "60 tpx"}
    },
    "OVRW": {
        "Twin": {"velocidad": 50, "intensidad": "90 tpx"},
        "Flexi-Maniquí": {"velocidad": 56, "intensidad": "70 tpx"},
        "Flexi-Mesa": {"velocidad": 45, "intensidad": "60 tpx"}
    }
}

# 2. LA LISTA DESPLEGABLE
lavado_elegido = st.selectbox("Selecciona el lavado:", ["DELT", "OVRW"])
st.header(f"Lavado actual: {lavado_elegido}")

# Sacamos los datos del archivero según lo que se eligió arriba
datos_actuales = datos_lavados[lavado_elegido]

# 3. Creamos las CUATRO pestañas (agregué la de fotos aquí)
tab1, tab2, tab3, tab4 = st.tabs(["Twin", "Flexi-Maniquí", "Flexi-Mesa", "📸 Comparativa"])

# Función para calcular los tiempos y turnos
def mostrar_info_maquina(nombre_maquina, pzas_por_hora, intensidad):
    st.subheader(f"⚙️ Máquina: {nombre_maquina}")
    
    segundos_totales = 3600 / pzas_por_hora
    minutos = int(segundos_totales // 60)
    segundos_restantes = int(segundos_totales % 60)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Velocidad", f"{pzas_por_hora} pzas / hora")
    with col2:
        st.metric("Intensidad", intensidad)
    with col3:
        st.metric("Tiempo por prenda", f"{minutos} min {segundos_restantes} seg")
        st.caption(f"({int(segundos_totales)} segundos totales)")
        
    st.write("---")
    st.subheader("📊 Metas de Producción")
    
    datos_turnos = {
        "Turno": ["1 Turno (8 horas)", "2 Turnos (15 horas)", "3 Turnos (24 horas)"],
        "Prendas Totales": [pzas_por_hora * 8, pzas_por_hora * 15, pzas_por_hora * 24]
    }
    
    st.table(pd.DataFrame(datos_turnos))

# 4. Llenamos las 3 pestañas de las máquinas
with tab1:
    mostrar_info_maquina("Twin", datos_actuales["Twin"]["velocidad"], datos_actuales["Twin"]["intensidad"])

with tab2:
    mostrar_info_maquina("Flexi-Maniquí", datos_actuales["Flexi-Maniquí"]["velocidad"], datos_actuales["Flexi-Maniquí"]["intensidad"])

with tab3:
    mostrar_info_maquina("Flexi-Mesa", datos_actuales["Flexi-Mesa"]["velocidad"], datos_actuales["Flexi-Mesa"]["intensidad"])

# 5. Llenamos la pestaña de fotos con búsqueda automática
with tab4:
    st.subheader(f"Vista Frontal - {lavado_elegido}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(f"fotos/{lavado_elegido}_frente_bmp.jpg", caption="Diseño Frente (BMP)")
    with col2:
        st.image(f"fotos/{lavado_elegido}_frente_lavado.jpg", caption="Resultado Frente (Lavado)")
        
    st.write("---") 
    
    st.subheader(f"Vista Trasera - {lavado_elegido}")
    col3, col4 = st.columns(2)
    
    with col3:
        st.image(f"fotos/{lavado_elegido}_trasera_bmp.jpg", caption="Diseño Trasera (BMP)")
    with col4:
        st.image(f"fotos/{lavado_elegido}_trasera_lavado.jpg", caption="Resultado Trasera (Lavado)")
