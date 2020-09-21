import json

in_file = open('eq_data_1_day_m1.json', 'r') #open file

out_file = open('readable_eq_data.json', 'w') #writing to a new file

eq_data = json.load(in_file) #loading the file, this creates a dictionary

json.dump(eq_data, out_file, indent=4) #taking the eq_data and putting it into the outfile

list_of_eqs = eq_data['features'] #we want a list of all of the earthquakes. eq_data is a dictionary, that has a key called features. 
                                    #The value for features is a list. When you call back the value in features, it will create a list.

print(type(list_of_eqs)) #output: <class 'list'>

print(len(list_of_eqs)) #the length of that list is how many earthquakes we have.

mags, lons, lats, hover_text = [], [], [], []#create three empty lists

for eq in list_of_eqs: #for earthquake (type:dictionary) in the list we created, each index in the list is apart of a dictionary called properties. mag, lon, lats are keys
    mag = eq['properties']['mag']
    title = eq['properties']['title']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

print('Mags')
print(mags[:10])

print('Lons')
print(lons[:10])

print('Lats')
print(lats[:10])

#############################################################
from plotly.graph_objs import Scattergeo, Layout #uses world maps
from plotly import offline

#data = [Scattergeo(lon=lons, lat=lats)] #Scattergeo needs these as arguments, basic data layouts

data =[{
    'type': 'scattergeo', 
    'lon': lons,
    'lat': lats, 
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],  #for each magnitude in the list of magnitudes, take that magnitude and multiply by 5
        'color': mags, 
        'colorscale': 'Viridis', 
        'reversescale': True, 
        'colorbar': {'title':'Magnitude'}
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')
