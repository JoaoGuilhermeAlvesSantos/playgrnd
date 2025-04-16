import json
import pandas as pd
import plotly.express as px

# Lê o arquivo JSON
with open("sorted_data.json", "r") as f:
    data = json.load(f)

# Converte o dicionário para DataFrame
events = data["total_events_by_country"]
df = pd.DataFrame(list(events.items()), columns=["country", "value"])


# Define categorias nomeadas para os tiers
def get_tier_label(val):
    if val < 50:
        return "Muito Baixo (<50)"
    elif val < 200:
        return "Baixo (50–199)"
    elif val < 600:
        return "Moderado (200–599)"
    elif val < 1500:
        return "Alto (600–1499)"
    else:
        return "Muito Alto (1500+)"


df["tier"] = df["value"].apply(get_tier_label)

# Paleta de cores correspondente aos nomes
tier_colors = {
    "Muito Baixo (<50)": "#FAF0CA",
    "Baixo (50–199)": "#F4D35E",
    "Moderado (200–599)": "#EE964B",
    "Alto (600–1499)": "#F95738",
    "Muito Alto (1500+)": "#00171F",
}

# Mapa com legenda categórica
fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="tier",
    color_discrete_map=tier_colors,
    title="Distribuição de Eventos por Região",
)

fig.write_html("../static/tiebe_potential_events_data.html")
fig.show()
