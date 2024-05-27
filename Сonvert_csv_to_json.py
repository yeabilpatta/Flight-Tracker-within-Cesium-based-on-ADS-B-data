import pandas as pd
import json
from google.colab import files

def convert_csv_to_json(csv_file):
    df = pd.read_csv(csv_file)
    
    df[['latitude', 'longitude']] = df['Position'].str.split(',', expand=True)
    
    df.rename(columns={'Altitude': 'height'}, inplace=True)
    
    json_data = df[['latitude', 'longitude', 'height']].to_dict(orient='records')
    
    return json_data

uploaded = files.upload()

csv_filename = next(iter(uploaded))

json_data = convert_csv_to_json(csv_filename)

json_filename = 'data.json'
with open(json_filename, 'w') as f:
    json.dump(json_data, f)

print("CSV data has been successfully converted to JSON and saved as 'data.json'.")

files.download(json_filename)