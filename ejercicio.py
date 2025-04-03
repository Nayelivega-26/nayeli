import numpy as np
import matplotlib.pyplot as plt

edades = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
media, mediana = np.mean(edades), np.median(edades)
varianza, std = np.var(edades), np.std(edades)

plt.bar(range(len(edades)), edades, color='skyblue', edgecolor='black')
plt.axhline(media, color='red', linestyle='dashed', label=f'Media: {media:.2f}')
plt.axhline(mediana, color='green', linestyle='dashed', label=f'Mediana: {mediana:.2f}')
plt.text(0, 78, f'Varianza: {varianza:.2f}\nDesviación Estándar: {std:.2f}', fontsize=12)
plt.legend()
plt.show()

print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Varianza: {varianza:.2f}, Desviación Estándar: {std:.2f}")
