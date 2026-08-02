# Ejemplo Análisis simple de retorno de inversión (ROI)

inversion_inicial = 10000  # USD
tasa_interes = 0.08        # 8% anual
anios = 5

# Cálculo de interés compuesto
monto_final = inversion_inicial * (1 + tasa_interes) ** anios
ganancia_neta = monto_final - inversion_inicial

# Imprimir resultados
print(f"Inversión inicial: ${inversion_inicial:,.2f}")
print(f"Monto acumulado tras {anios} años: ${monto_final:,.2f}")
print(f"Ganancia neta: ${ganancia_neta:,.2f}")

# Conclusión / Recomendación al inversionista
if ganancia_neta > 3000:
    print("\nRecomendación: El proyecto genera un retorno atractivo y supera la meta mínima de rendimiento. Se sugiere proceder con la inversión.")
else:
    print("\nRecomendación: El rendimiento es moderado. Se sugiere evaluar opciones con mayor tasa de retorno.")