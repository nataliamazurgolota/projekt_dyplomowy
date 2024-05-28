import pandas as pd
import json

def read_json(path: str) -> dict:
    with open(path, 'r') as file:
        return json.load(file)

config = read_json('/home/student/PycharmProjects/projekt_dyplomowy/projekt_dyplomowy/config_files/config.json')
nypd_data_config = config['datasets']['nypd_data']
nypd_data_dtypes = nypd_data_config['dtypes']
nypd_data_dir = nypd_data_config['directory']

nypd_data = pd.read_csv(nypd_data_dir,
                       dtype=nypd_data_dtypes,
                       usecols=[*nypd_data_dtypes])

print(nypd_data)
