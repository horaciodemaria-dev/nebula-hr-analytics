# app/csv_writer.py

import pandas as pd

def write_csv(data: list, filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
