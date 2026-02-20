# app/main.py

from fastapi import FastAPI
from app.data_loader import load_employees
from typing import Optional

app = FastAPI(title="NebulaWorks HR Analytics API")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "NebulaWorks HR API"
    }

@app.get("/employees")
def get_employees(
    limit: int = 20,
    offset: int = 0,
    department: Optional[str] = None,
    is_active: Optional[bool] = None,
):
    df = load_employees()

    # 🔎 Filtros
    if department:
        df = df[df["department"] == department]

    if is_active is not None:
        df = df[df["is_active"] == int(is_active)]

    total = len(df)

    page = df.iloc[offset : offset + limit]

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "filters": {
            "department": department,
            "is_active": is_active,
        },
        "data": page.to_dict(orient="records"),
    }


@app.get("/stats/summary")
def summary():
    df = load_employees()

    return {
        "total_employees": int(len(df)),
        "active_employees": int(df["is_active"].sum()),
        "avg_salary": round(float(df["salary_usd"].mean()), 2),
    }
