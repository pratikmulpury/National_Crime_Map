import pandas as pd
from shapely.geometry import Point, Polygon
import json
import os
import numpy as np

datapath = os.path.dirname(__file__)
beatspath = os.path.join(datapath, 'durham_2018_geojson.csv')
crimepath = os.path.join(datapath, 'durham_2018_crime.csv')

df_beats = pd.read_csv(beatspath)
df_crime = pd.read_csv(crimepath)

shape_map = {}
for i in range(np.shape(df_beats)[0]):
    row = df_beats.iloc[i,:]
    id = row.loc['id']
    js = json.loads(row.loc['geojson'])
    coordinates = js["coordinates"][0] # list of lists
    tuple_coor = []
    for l in coordinates:
        tuple_coor.append((l[0],l[1]))
    shape_map[id] = Polygon(tuple_coor)

new_map = {}
new_map['incident_id'] = []
new_map['district_id'] = []

# for dis_id in shape_map:
#     print(shape_map[dis_id].area)

for i in range(np.shape(df_crime)[0]):
    row = df_crime.iloc[i,:]
    inc_id = row.loc['incident_id']
    point = Point((row.loc['latitude'], row.loc['longitude']))
    for dis_id in shape_map:
        if shape_map[dis_id].contains(point):
            new_map['incident_id'].append(inc_id)
            new_map['district_id'].append(dis_id)
            break

new_df = pd.DataFrame(new_map)
new_df.to_csv(os.path.join(datapath, "durham_2018_dc.csv"), index=False)

# for point in df['Geo Shape']:
#     pos = [float(ele) for ele in points[0].split(", ")]
#     cur_point = Point(pos)
#     for feature in js['features']:
#         polygon = Polygon(feature['geometry'])
