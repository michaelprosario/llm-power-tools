# read csv of import_data

import pandas as pd
import json

df = pd.read_csv('podcast_data.csv')

# read "Id" and "Source" data into a row.. Iterate over the rows of the CSV
for index, row in df.iterrows():
    id = row['Id']
    source = row['Source']

    source_json = json.loads(source)
    content_source_id = source_json["ContentSourceId"]
    title = source_json["Title"]
    source_url = source_json["SourceUrl"]
    description = source_json["Description"]    
    enclosure_url = source_json["EnclosureUrl"]    
    
    json_data = {
        "Id": id,
        "ContentSourceId": content_source_id,
        "Title": title,
        "SourceUrl": source_url,
        "Description": description,
        "EnclosureUrl": enclosure_url
    }

    with open(f"podcastData/podcast_{id}.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
