import json
import pandas as pd
import plotly.express as px

# Lê o arquivo JSON
with open('sorted_data.json', 'r') as f:
    data = json.load(f)

# Converte o dicionário para DataFrame
events = data['total_events_by_country']
df = pd.DataFrame(list(events.items()), columns=['country', 'value'])

# Cria o mapa
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='value',
    color_continuous_scale='hot_r',
    title='Eventos por País'
)

fig.write_html("static/mapa_mundi.html")
