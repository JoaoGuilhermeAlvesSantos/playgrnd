import pandas as pd
import matplotlib.pyplot as plt

# Dados
total_events_by_year = {
    "2015": 1729,
    "2016": 1464,
    "2017": 1963,
    "2018": 2661,
    "2019": 3140,
    "2020": 6501,
    "2021": 5481,
    "2022": 4589,
    "2023": 5866,
    "2024": 9700,
    "2025": 3375
}

# Converter para DataFrame
df = pd.DataFrame(list(total_events_by_year.items()), columns=["Ano", "Eventos"])
df["Ano"] = df["Ano"].astype(int)
df = df.sort_values("Ano")

# Mostrar a tabela
print(df.to_string(index=False))

# Criar gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Ano"], df["Eventos"], color="#005f99")

# Adicionar rótulos nas barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f'{yval}', ha='center', va='bottom', fontsize=9)

# Configurações do gráfico
plt.title("Total Events by Year (2015-2025)", fontsize=16)
plt.xlabel("Years")
plt.ylabel("Events")
plt.xticks(df["Ano"], rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
