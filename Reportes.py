import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime
import os


if not os.path.exists("datos_ventas.csv"):
    with open("datos_ventas.csv", "w") as f:
        f.write("fecha,ventas\n")
        f.write("2025-08-15,1200\n")
        f.write("2025-08-16,950\n")
        f.write("2025-08-17,1100\n")
        f.write("2025-08-18,1300\n")
        f.write("2025-08-19,1250\n")
        f.write("2025-08-20,1400\n")
        f.write("2025-08-21,1500\n")

# 📁 Cargar datos
df = pd.read_csv("datos_ventas.csv")  # Asegurate de tener este archivo

# 📅 Filtrar última semana
hoy = datetime.date.today()
una_semana = hoy - datetime.timedelta(days=7)
df['fecha'] = pd.to_datetime(df['fecha'])
df_semana = df[df['fecha'].dt.date >= una_semana]

# 📊 Generar gráfico
plt.figure(figsize=(10, 6))
ventas_por_dia = df_semana.groupby(df_semana['fecha'].dt.date)['ventas'].sum()
ventas_por_dia.plot(kind='bar', color='skyblue')
plt.title("Ventas por día (última semana)")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("grafico_ventas.png")
plt.close()

# 📄 Crear PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Reporte Semanal de Ventas", ln=True, align='C')
pdf.image("grafico_ventas.png", x=10, y=30, w=180)
pdf.output("Reporte_Semanal.pdf")

print("✅ Reporte generado exitosamente.")

