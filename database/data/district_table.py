import pandas as pd
import os
import json
import numpy as np

datapath = os.path.dirname(__file__)
rawpath = os.path.join(datapath, "..", "raw")

SCHEMA_LIST = ['id', 'LAWBEAT', 'Geo Shape', 'CONTIGUOUS', 'LAWDIST']

df = pd.read_csv(os.path.join(rawpath, "police-beats.csv"), sep=";")
df = df[df['CONTIGUOUS']=='yes']
num_rows = np.shape(df)[0]
id_list = list(range(0,num_rows))
df['id'] = pd.Series(id_list, df.index)

df = df[SCHEMA_LIST]

df = df.rename(columns = {"LAWBEAT": "law_beat", "Geo Shape": "geojson", "CONTIGUOUS": "contiguous", "LAWDIST": "district"})
df.to_csv(os.path.join(datapath, "durham_2018_geojson.csv"), index=False, header=True)

SCHEMA_CLEAN = ['id', 'law_beat', 'contiguous', 'district']
df =df[SCHEMA_CLEAN]

df.to_csv(os.path.join(datapath, "durham_2018_districts.csv"), index=False, header=True)
