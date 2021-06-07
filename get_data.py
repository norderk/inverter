import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data/Inverter Data Set.csv')


def get_data():
    return pd.read_csv(FILE_PATH)

print(get_data().head(5))