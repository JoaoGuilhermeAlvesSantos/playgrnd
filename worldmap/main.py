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
    color_continuous_scale='deep',
    title='Eventos por País'
)

fig.write_html("../static/tiebe_potential_events_data.html")
fig.show()