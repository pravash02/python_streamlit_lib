import json
import pandas as pd


with open('./test_file.json', 'r') as f:
    json_data = json.load(f)


data = json_data['data']

formated_data = []
for entry in data:
    entry_list = []
    prefix_list = [entry.get('customerid'), True if entry.get('isvip') else False]
    for k in entry.keys():
        if 'site' in k:
            for timestamp in entry[k]:
                tmp = [k, timestamp]
                entry_list.append(prefix_list + tmp)
    formated_data.extend(entry_list)

print(formated_data)

df = pd.DataFrame(formated_data, columns=['customerid', 'isvip', 'siteid', 'timestamp'])
print(df)
