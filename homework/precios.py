# homework/precios.py

import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


def generar_grafico_precios():
    # Crear carpeta si no existe
    Path("files/images").mkdir(parents=True, exist_ok=True)

    # Datos de ejemplo (puedes personalizarlos)
    data = {
        "Producto": ["Bolsa A", "Bolsa B", "Bolsa C", "Bolsa D", "Bolsa E"],
        "Precio": [4200, 3900, 4500, 4100, 4000]
    }
    df = pd.DataFrame(data)

    # Crear gráfico
    plt.figure(figsize=(8, 5))
    barras = plt.bar(df["Producto"], df["Precio"], color="mediumseagreen")
    plt.title("Precios de bolsas")
    plt.xlabel("Producto")
    plt.ylabel("Precio ($)")
    plt.grid(axis='y', linestyle="--", alpha=0.5)

    # Etiquetas encima de cada barra
    for barra in barras:
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 50,
                 f"${barra.get_height()}", ha='center', va='bottom')

    # Guardar gráfico
    plt.tight_layout()
    plt.savefig("files/images/precios.png")
    plt.close()
