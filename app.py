import streamlit as st
import pandas as pd

st.title("👖 Sistema de Producción Láser")

# 1. EL ARCHIVERO (Diccionario con el DELT y el nuevo OVRW con su link)
datos_lavados = {
    "DELT": {
        "Twin": {"velocidad": 40, "intensidad": "90 tpx"},
        "Flexi-Maniquí": {"velocidad": 46, "intensidad": "70 tpx"},
        "Flexi-Mesa": {"velocidad": 35, "intensidad": "60 tpx"},
        "link": "https://docs.google.com/spreadsheets/d/1Y6INggv8Uvjk3BJ7FHHxmSnOfG6_5_nm/edit?usp=drive_link&ouid=114257330921113170270&rtpof=true&sd=true"
    },
    "OVRW": {
        "Twin": {"velocidad": 50, "intensidad": "90 tpx"},
        "Flexi-Maniquí": {"velocidad": 56, "intensidad": "70 tpx"},
        "Flexi-Mesa": {"velocidad": 45, "intensidad": "60 tpx"},
        "link": "https://docs.google.com/spreadsheets/d/1Prj7bx7A2aPpMWt7ZnB8rbPa52KFkK0o/edit?usp=drive_link&ouid=114257330921113170270&rtpof=true&sd=true"
    }
}

# 2. LA LISTA DESPLEGABLE (Con opción vacía por defecto)
# Agregamos "Selecciona un lavado..." al principio de la lista
opciones = ["Selecciona un lavado...", "DELT", "OVRW"]
lavado_elegido = st.selectbox("Selecciona el lavado:", opciones)

# 3. CONDICIÓN DE ESPERA
# Si el usuario no ha elegido nada, mostramos un mensaje y detenemos el código aquí
if lavado_elegido == "Selecciona un lavado...":
    st.info("👈 Por favor, selecciona un lavado en el menú de arriba para ver su información.")
    st.stop() # Esto detiene la página para que no se vea nada más abajo

# Si el código llega hasta aquí, es porque ya eligieron un lavado válido (DELT u OVRW)
st.header(f"Lavado actual: {lavado_elegido}")

# Sacamos los datos del archivero según lo que se eligió arriba
datos_actuales = datos_lavados[lavado_elegido]

# 4. Creamos las CINCO pestañas
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Twin", "Flexi-Maniquí", "Flexi-Mesa", "📸 Comparativa", "🧪 Fórmula"])

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

# Llenamos las 3 pestañas de las máquinas
with tab1:
    mostrar_info_maquina("Twin", datos_actuales["Twin"]["velocidad"], datos_actuales["Twin"]["intensidad"])

with tab2:
    mostrar_info_maquina("Flexi-Maniquí", datos_actuales["Flexi-Maniquí"]["velocidad"], datos_actuales["Flexi-Maniquí"]["intensidad"])

with tab3:
    mostrar_info_maquina("Flexi-Mesa", datos_actuales["Flexi-Mesa"]["velocidad"], datos_actuales["Flexi-Mesa"]["intensidad"])

# Llenamos la pestaña de fotos dinámicas
with tab4:
    st.subheader(f"Vista Frontal - {lavado_elegido}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(f"fotos/{lavado_elegido}_frente_bmp.jpg", caption="Diseño Frente (BMP)")
    with col2:
        st.image(f"fotos/{lavado_elegido}_frente_lavado.jpg", caption="Resultado Frente (Lavado
