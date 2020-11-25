import folium
from folium import plugins
import math
import pandas as pd

data1 = pd.read_csv("/Users/ericoliverio/Desktop/daily_report.csv")
#-

data1.dropna(inplace=True)
data1
#-

map = folium.Map(location=[42.895, -78.8815],tiles='stamentoner',zoom_start=11,name='Test')

cluster = plugins.MarkerCluster(name='% of Cases by ZIP',show=False).add_to(map)
#feature_group1 = folium.FeatureGroup("ZIP Codes")

tooltip = 'Click to expand '

for index, row in data1.iterrows():
    
    df = pd.DataFrame(data=[[int(row['Total Cases'])],[int(row['Daily Cases'])],[str(round(100*row['Total Cases']/row['Population'],1))+'%'],[round(row['GF'],1)]], columns=[str(row['Name'])+': '+str(row['Zip Code'])],index=['Total Cases','Daily Cases','% Infected','Growth Factor'])
    #df.set_index('')
    html = df.to_html(classes='table table-striped table-hover table-condensed table-responsive')

    popup1 = folium.Popup(html)
    
    folium.CircleMarker([row['X'], row['Y']],
    radius= 1500*row['Total Cases']/row['Population'],
                        #popup=str(row['Neighborhood'])+': '+str(row['Daily Cases'])+' new cases. '+str(round(100*row['Total Cases']/row['Population'],1))+'% infected',
    popup=popup1,
    tooltip=tooltip,
    fill_color="#3db7e4" # divvy color
    ).add_to(cluster)

#map.add_child(feature_group1)

feature_group = folium.FeatureGroup("Daily Cases Heat Map",show=False)

#for index, row in data1.iterrows():
stationArr = data1[['X', 'Y','Daily Cases']].as_matrix()
    #print(row['Total Cases'])
feature_group.add_child(plugins.HeatMap(stationArr,blur=33,radius=40))
   
map.add_child(feature_group)

folium.LayerControl(collapsed=False).add_to(map)

map.save("/Users/ericoliverio/Desktop/erie_covid.html")
print('map saved')