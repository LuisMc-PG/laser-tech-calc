# --- CALCULADORA DE PRODUCCIÓN LÁSER (LAVADO DELT) ---

# 1. Definimos la velocidad de cada máquina (prendas por hora)
VELOCIDAD_TWIN = 40
VELOCIDAD_FLEXI_MANIQUI = 48
VELOCIDAD_FLEXI_MESA = 36

# 2. Definimos las intensidades (estos datos son fijos para este lavado)
INTENSIDAD_TWIN = 100
INTENSIDAD_FLEXI_MANIQUI = 80
INTENSIDAD_FLEXI_MESA = 68

# 3. Calculamos la producción para diferentes turnos (8, 15 y 24 horas)
turnos_horas = [8, 15, 24]

print("--- RESULTADOS DE PRODUCCIÓN (LAVADO DELT) ---\n")

# Usamos un 'bucle' para calcular cada turno automáticamente
for horas in turnos_horas:
    print(f"=== RESULTADOS PARA UN TURNO DE {horas} HORAS ===")
    
    # Cálculos: Total de prendas = Velocidad x Horas
    total_twin = VELOCIDAD_TWIN * horas
    total_flexi_mani = VELOCIDAD_FLEXI_MANIQUI * horas
    total_flexi_mesa = VELOCIDAD_FLEXI_MESA * horas
    
    # Mostramos los resultados en la pantalla
    print(f"- Máquina TWIN (con maniquí):")
    print(f"  > Producción: {total_twin} prendas")
    print(f"  > Intensidad (manual): {INTENSIDAD_TWIN} tpx")
    print("-" * 20)
    
    print(f"- Máquina FLEXI (con maniquí):")
    print(f"  > Producción: {total_flexi_mani} prendas")
    print(f"  > Intensidad (manual): {INTENSIDAD_FLEXI_MANIQUI} tpx")
    print("-" * 20)
    
    print(f"- Máquina FLEXI (en mesa):")
    print(f"  > Producción: {total_flexi_mesa} prendas")
    print(f"  > Intensidad (manual): {INTENSIDAD_FLEXI_MESA} tpx")
    print("=" * 30 + "\n")

print("--- Fin de los cálculos ---")
