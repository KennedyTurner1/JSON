import json

infile  = open('US_fires_9_14.json', 'r')

fire_data = json.load(infile)

lats, lons, brights = [], [], []

for fire in fire_data: #for dictionary in list fire_data
    bright = float(fire['brightness'])
    lat = float(fire['latitude'])
    lon = float(fire['longitude'])
    if bright > 450:
        brights.append(bright)
        lats.append(lat)
        lons.append(lon)

#create the geo map 

from plotly.graph_objs import Scattergeo, Layout #uses world maps
from plotly import offline

data =[{
    'type': 'scattergeo', 
    'lon': lons,
    'lat': lats, 
    'marker': {
        'size': [1/30*bright for bright in brights],  #for each fire in the list of fires over 450, take the size of the fire and multiply by 5
        'color': brights, 
        'colorscale': 'Viridis', 
        'reversescale': True, 
        'colorbar': {'title':'Brightness'}
    }
}]

my_layout = Layout(title='2020 Fires between September 14-20')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='US_Fires_9_14.html')