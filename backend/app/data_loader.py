# app/data_loader.py

import pandas as pd
from pathlib import Path
import numpy as np

DATA_PATH = Path(__file__).parent.parent / "data" / "employees.csv"

def load_employees() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    # Convertir fechas manualmente
    for col in ["hire_date", "termination_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
        df[col] = df[col].dt.strftime("%Y-%m-%d")

    # 🔥 LIMPIEZA FINAL ABSOLUTA
    df = df.replace(
        {
            np.nan: None,
            pd.NaT: None,
        }
    )

    return df
