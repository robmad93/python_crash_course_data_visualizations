import os
import pandas as pd
import plotly.express as px

os.chdir("C:/Users/robma/Desktop/Python/data_visualization")  # Change to file path.

filename = "data/MODIS_C6_1_Europe_7d.csv"

# Read CSV file into a pandas DataFrame
df = pd.read_csv(filename)

# Map the wildfires using Plotly Express
fig = px.density_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    z="frp",  # Assuming "frp" is the column name for fire radiative power
    radius=20,
    center=dict(lat=42.83, lon=-8.35),
    zoom=8,
    mapbox_style="open-street-map",
    title="European wildfires - July, 2024",
)

fig.show()
