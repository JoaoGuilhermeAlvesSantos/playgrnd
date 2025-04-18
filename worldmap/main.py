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
    if val <= 50:
        return "Lowest [0–50]"
    elif val <= 200:
        return "Low [51–200]"
    elif val <= 600:
        return "Moderate [201–600]"
    elif val <= 1500:
        return "High [601–1500]"
    else:
        return "Highest [1500+]"


df["tier"] = df["value"].apply(get_tier_label)

# Paleta de cores correspondente aos nomes
tier_colors = {
    "Lowest [0–50]": "#FAF0CA",
    "Low [51–200]": "#F4D35E",
    "Moderate [201–600]": "#EE964B",
    "High [601–1500]": "#F95738",
    "Highest [1500+]": "#00171F",
}

# Mapa com legenda categórica
fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="tier",
    color_discrete_map=tier_colors,
    title="Worldwide Distribution of TiEBe Events (2015–2025)",
    hover_data={"value": True, "tier": False},  # Mostra só o value no hover
)

fig.write_html("../static/tiebe_potential_events_data.html")
fig.show()
