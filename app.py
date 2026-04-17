import streamlit as st
import pandas as pd

st.title("👖 Sistema de Producción Láser")
st.header("Lavado: DELT")

# Creamos las 3 pestañas para las máquinas
tab1, tab2, tab3 = st.tabs(["Twin", "Flexi-Maniquí", "Flexi-Mesa"])

# Función para calcular y mostrar la información de cada máquina sin repetir código
def mostrar_info_maquina(nombre_maquina, pzas_por_hora, intensidad):
    st.subheader(f"⚙️ Máquina: {nombre_maquina}")
    
    # Cálculos de tiempo por prenda
    segundos_totales = 3600 / pzas_por_hora
    minutos = int(segundos_totales // 60)
    segundos_restantes = int(segundos_totales % 60)
    
    # Mostramos Velocidad, Intensidad y Tiempos en 3 columnas
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
    
    # Calculamos cuánto se hace en 8, 15 y 24 horas
    datos_turnos = {
        "Turno": ["1 Turno (8 horas)", "2 Turnos (15 horas)", "3 Turnos (24 horas)"],
        "Prendas Totales": [pzas_por_hora * 8, pzas_por_hora * 15, pzas_por_hora * 24]
    }
    
    # Mostramos los resultados en una tabla
    st.table(pd.DataFrame(datos_turnos))

# Metemos la información exacta que me diste en cada pestaña
with tab1:
    mostrar_info_maquina("Twin", 40, "90 tpx")

with tab2:
    mostrar_info_maquina("Flexi-Maniquí", 46, "70 tpx")

with tab3:
    mostrar_info_maquina("Flexi-Mesa", 35, "60 tpx")
