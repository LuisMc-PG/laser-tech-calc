import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Laser Tech Calc", page_icon="🔥")

# Título y Créditos
st.title("🔥 Laser Tech Calculator")
st.markdown("### Desarrollado por: **Luis Mc**")
st.write("Consulta tiempos, intensidades y potencial de producción al instante.")

# Base de Datos (Aquí puedes agregar más después)
base_datos = {
    "DELT": {"tiempo": 110, "intensidad": "45%", "desc": "Lavado DELT Estándar"},
    "OVRW": {"tiempo": 120, "intensidad": "52%", "desc": "Overwash Pesado"},
    "STND": {"tiempo": 90, "intensidad": "38%", "desc": "Standard Light"},
    "DARK": {"tiempo": 150, "intensidad": "60%", "desc": "Dark Denim Laser"}
}

# Buscador
busqueda = st.text_input("Escribe el nombre del lavado:", placeholder="Ej. DELT").upper()

if busqueda:
    if busqueda in base_datos:
        datos = base_datos[busqueda]
        t = datos['tiempo']
        
        st.success(f"Resultados para: {busqueda}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tiempo de Marcado", f"{t} seg")
        with col2:
            st.metric("Intensidad Láser", datos['intensidad'])
            
        st.info(f"**Descripción:** {datos['desc']}")

        # Tabla de Producción
        st.write("---")
        st.subheader("Potencial de Producción")
        horas = [8, 10, 12, 24]
        produccion = [int((h * 3600) / t) for h in horas]
        
        df = pd.DataFrame({
            "Jornada Laboral": [f"{h} Horas" for h in horas],
            "Prendas Totales": [f"{p} pzas" for p in produccion]
        })
        st.table(df)
    else:
        st.error("Lavado no encontrado. Contacta a Luis Mc para darlo de alta.")

st.markdown("---")
st.caption("© 2026 Sistema de Gestión Láser - Atotonilco de Tula, Hgo.")
