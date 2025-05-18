# homework/visualization.py

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def make_price_plot():
    # Crear carpetas si no existen
    Path("files/images").mkdir(parents=True, exist_ok=True)

    # Datos de ejemplo: precios por producto
    data = {
        "Producto": ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"],
        "Precio": [1200, 950, 1600, 1100, 1300]
    }
    df = pd.DataFrame(data)

    # Gráfico
    plt.figure(figsize=(8, 5))
    bars = plt.bar(df["Producto"], df["Precio"], color="skyblue")
    plt.title("Precios por producto")
    plt.xlabel("Producto")
    plt.ylabel("Precio ($)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Etiquetas en las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 20, f"${height}", ha='center', va='bottom')

    # Guardar la imagen
    plt.tight_layout()
    plt.savefig("files/images/precios.png")
    plt.close()
