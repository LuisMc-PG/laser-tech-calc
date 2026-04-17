import streamlit as st
import pandas as pd

st.title("👖 Sistema de Producción Láser")
st.header("Lavado: DELT")

# Creamos las 3 pestañas para las máquinas
tab1, tab2, tab3 = st.tabs(["Twin", "Flexi Maniquí", "Flexi Mesa"])

# Función para no repetir código y hacer los cálculos de los turnos
def calcular_produccion(nombre_maquina, pzas_por_hora):
    st.subheader(f"⚙️ Máquina: {nombre_maquina}")
    st.metric("Velocidad", f"{pzas_por_hora} prendas por hora")
    
    # Calculamos cuánto se hace en 8, 15 y 24 horas
    datos_turnos = {
        "Turno": ["1 Turno (8 horas)", "2 Turnos (15 horas)", "3 Turnos (24 horas)"],
        "Prendas Totales": [pzas_por_hora * 8, pzas_por_hora * 15, pzas_por_hora * 24]
    }
    
    # Mostramos los resultados en una tabla
    st.table(pd.DataFrame(datos_turnos))

# Metemos la información de cada máquina en su pestaña correspondiente
with tab1:
    calcular_produccion("Twin", 40)

with tab2:
    calcular_produccion("Flexi Maniquí", 46)

with tab3:
    calcular_produccion("Flexi Mesa", 35)
