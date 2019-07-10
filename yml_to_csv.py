import yaml 
import pandas as pd 
import sys

level_1_name = []
transa_csv = 'transaction-specification.csv'

# level 2 category name to level1 category name form data.yml file
def level2_to_level1(level_2_name):
    with open('data.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for key, value in data.items():
            if value["name"].lower() == level_2_name.lower():
                p_name = value["parent"]["name"]
                return p_name
            
# list of level2 category as category list of csv file
f = pd.read_csv(transa_csv)
categories = f['category']
for category in categories:
    print("Level2: ",category)
    level1 = level2_to_level1(category)
    print("level1 ", level1)
    level_1_name.append(level1)


# new column of level1 category
f['Level 1'] = level_1_name
f.to_csv('trans2.csv', index=False)