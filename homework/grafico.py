# homework/grafico.py

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def generar_grafico_precios():
    Path("files/images").mkdir(parents=True, exist_ok=True)

    data = {
        "Bolsa": ["Bolsa A", "Bolsa B", "Bolsa C", "Bolsa D", "Bolsa E"],
        "Precio": [4200, 3900, 4500, 4100, 4000]
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(8, 5))
    barras = plt.bar(df["Bolsa"], df["Precio"], color="cornflowerblue")
    plt.title("Precios de bolsas")
    plt.xlabel("Tipo de bolsa")
    plt.ylabel("Precio ($)")
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for barra in barras:
        plt.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 50,
                 f"${barra.get_height():,.0f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig("files/images/precios.png")
    plt.close()


