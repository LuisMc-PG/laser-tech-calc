with tab4:
        if seleccion in formulas_maestras:
            f = formulas_maestras[seleccion]
            st.success(f"📋 COMPARATIVA TÉCNICA DE DISEÑO VS RESULTADO: {seleccion}")
            
            def buscar_img(nombre_base):
                for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG']:
                    if os.path.exists(nombre_base + ext): return nombre_base + ext
                return None

            # --- FILA 1: COMPARATIVA FRONTAL ---
            st.subheader("👕 VISTA FRONTAL")
            col1, col2 = st.columns(2)
            with col1:
                img = buscar_img(f"{seleccion}_frente_bmp")
                if img: st.image(img, caption="1. DISEÑO BMP (Frente)", use_container_width=True)
                else: st.info("Esperando BMP Frente...")
            
            with col2:
                img = buscar_img(f"{seleccion}_frente_lavado")
                if img: st.image(img, caption="2. LAVADO FINAL (Frente)", use_container_width=True)
                else: st.info("Esperando Foto Lavado Frente...")

            st.divider()

            # --- FILA 2: COMPARATIVA TRASERA ---
            st.subheader("👖 VISTA TRASERA")
            col3, col4 = st.columns(2)
            with col3:
                img = buscar_img(f"{seleccion}_trasera_bmp")
                if img: st.image(img, caption="3. DISEÑO BMP (Trasera)", use_container_width=True)
                else: st.info("Esperando BMP Trasera...")

            with col4:
                img = buscar_img(f"{seleccion}_trasera_lavado")
                if img: st.image(img, caption="4. LAVADO FINAL (Trasera)", use_container_width=True)
                else: st.info("Esperando Foto Lavado Trasera...")
            
            st.divider()
            
            # --- DATOS TÉCNICOS Y TABLA (Igual que antes) ---
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**D R Y   P R O C E S S:**")
                for p in f["Dry Process"]: st.write(f"• {p}")
            with col_b:
                st.write("**DATOS TÉCNICOS:**")
                st.write(f"Tela: {f['Info']['Tela']}\nPeso: {f['Info']['Peso']}\nPiezas: {f['Info']['Pzas']}")

            st.write("**L A V A N D E R Í A:**")
            st.table(pd.DataFrame(f["Lavanderia"]))
