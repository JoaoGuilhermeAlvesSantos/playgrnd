import json
import pandas as pd
import plotly.express as px

file_name = "sorted_data_2025.json"
with open(file_name, "r") as f:
    data = json.load(f)

fn = file_name.split(".")[0]
prefix = fn.split("sorted_")[1]

# Converte o dicionário para DataFrame
events = data['total_events_by_country']
df = pd.DataFrame(list(events.items()), columns=['country', 'value'])

# Cria o mapa
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='value',
    color_continuous_scale='teal',
    title=f'Worldwide Distribution of TiEBe Events {prefix.split("data_")[1]}',
)

fig.write_html(f"../static/tiebe_potential_events_{prefix}.html")
fig.show()