import pandas as pd
import os

datapath = os.path.dirname(__file__)
rawpath = os.path.join(datapath, "..", "raw")

SCHEMA_LIST = [
'longitude',
'latitude',
'incident_id',
'date',
'time',
'timestamp',
'description',
'type'
]

TYPE_ONE_CRIME = ['AGGRAVATED ASSAULT', 'LARCENY', 'BREAK IN', 'RAPE', 'ROBBERY', 'ROBB',
'CARJACK', 'ARSON', 'STOLEN VEHICLE', 'STABBING', 'ABDUCTION',
'KIDNAP', 'HOME INVASION', 'HOSTAGE', 'MURDER', 'HOMICIDE', 'MANSLAUGHTER']

# result = []
# for i in TYPE_ONE_CRIME:
#     result.append('%'+ i.lower() + '%')
# print(result)
#
# MURDER_KEYWORDS = ['MURDER', 'HOMICIDE', 'MANSLAUGHTER']
# ROBBERY_KEYWORDS = ['ROBBERY', 'ROBB', 'CARJACK']
# ASSAULT_KEYWORDS = ['AGGRAVATED ASSAULT', 'KIDNAP', 'ABDUCTION', 'STABBING']
# RAPE_KEYWORDS = ['RAPE']
#
# VIOLENT_CRIME = MURDER_KEYWORDS + ROBBERY_KEYWORDS + ASSAULT_KEYWORDS + RAPE_KEYWORDS

df = pd.read_csv(os.path.join(rawpath, "durham-police-crime-reports.csv"), sep = ';', dtype = {'hour_occu': str, 'monthstamp': str, 'yearstamp': str})
df = df[df['date_rept'].str.contains('2018')].drop_duplicates()
df['monthstamp'] = df['monthstamp'].apply(lambda x: str(x).zfill(2))
df['date'] = [str(a).split('T')[0] for a in df['date_occu']]
df['time'] = [b[0:2] + ":" + b[2:4] for b in df['hour_occu']]
df['timestamp'] = [str(a).split('T')[0] + " " + b[0:2] + ":" + b[2:4] for a,b in zip(df['date_occu'], df['hour_occu'])]

# def categorize(df, keyword_list):
#     res = []
#     for x1, x2 in zip(df['chrgdesc'], df['reportedas']):
#         full_des = str(x1) + str(x2)
#         current = 0
#         for y in keyword_list:
#             if y in full_des:
#                 current = 1
#                 break
#         res.append(current)
#     assert len(df['chrgdesc']) == len(res)
#     return res
#
# type_one_list = categorize(df, TYPE_ONE_CRIME)
# murder_list = categorize(df, MURDER_KEYWORDS)
# robbery_list = categorize(df, ROBBERY_KEYWORDS)
# assault_list = categorize(df, ASSAULT_KEYWORDS)
# rape_list = categorize(df, RAPE_KEYWORDS)
# violent_list = categorize(df, VIOLENT_CRIME)

# df['type_one'] = pd.Series(type_one_list, df.index)
# df['murder'] = pd.Series(murder_list, df.index)
# df['robbery'] = pd.Series(robbery_list, df.index)
# df['assault'] = pd.Series(assault_list, df.index)
# df['rape'] = pd.Series(rape_list, df.index)
# df['violent'] = pd.Series(violent_list, df.index)

x_list = []
y_list = []
for x in df['Geo Point']:
    splitted = str(x).split(", ")
    x_list.append(float(splitted[0]))
    y_list.append(float(splitted[1]))

df['longitude'] = x_list
df['latitude'] = y_list

df = df.rename(columns = {"Geo Point": "geo_point", "inci_id": "incident_id", "chrgdesc": "description", "reportedas": "type"})

df = df[SCHEMA_LIST]

df.to_csv(os.path.join(datapath, "durham_2018_crime.csv"), index=False, header=True)
