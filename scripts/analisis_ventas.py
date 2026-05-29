import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos/dataset.csv')
ventas_totales = df['monto_total'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
ventas_por_producto = df.groupby('producto')['monto_total'].sum()
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
df['mes'] = df['fecha_venta'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['monto_total'].sum()

plt.figure(figsize=(10, 5))
ventas_por_mes.plot(kind='bar', color='steelblue')
plt.title('Evolución de Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Monto Total ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
