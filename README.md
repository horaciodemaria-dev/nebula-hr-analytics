# Nebula HR Analytics

A small REST API that serves a synthetic HR dataset (1,000 fictional employees) with filtering, pagination and summary statistics, plus the script that generates that dataset.

**Stack:** Python · FastAPI · pandas · Faker · Uvicorn

> All data is randomly generated. No real people or companies are involved.

## Project structure

| Folder | What it does |
| --- | --- |
| `backend/` | FastAPI service. Reads `backend/data/employees.csv` and exposes it through the endpoints below. |
| `data-generator/` | Script that generates the synthetic dataset. See its [README](data-generator/README.md). |

## The dataset

1,000 employees for a fictional company ("NebulaWorks"):

- 5 departments: Engineering, Data, HR, Sales, Finance
- 5 cities in Latin America: Montevideo, Buenos Aires, Santiago, Bogotá, Lima
- 4 seniority levels (Junior, Mid, Senior, Lead), each with its own salary range in USD
- About 15% of employees have a termination date (`is_active = false`)

Columns: `employee_id`, `employee_code`, `alias`, `department`, `role`, `seniority`, `salary_usd`, `hire_date`, `termination_date`, `city`, `country`, `performance_score`, `employment_type`, `is_active`.

## Quick start

The repository already includes a dataset, so you can run the API right away. You need Python 3.11 or newer (the pinned pandas and NumPy versions require it).

```bash
cd backend
python -m venv venv
source venv/bin/activate          # Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- API: <http://127.0.0.1:8000>
- Interactive docs (Swagger UI): <http://127.0.0.1:8000/docs>

### Generate a new dataset (optional)

```bash
cd data-generator
python -m venv venv
source venv/bin/activate          # Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generate.py

# The API reads its own copy of the file, so copy the new one over it:
cp employees.csv ../backend/data/employees.csv      # Windows: copy employees.csv ..\backend\data\employees.csv
```

The generator is not seeded, so every run produces a different dataset (and different summary numbers).

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Health check. |
| `GET` | `/employees` | Paginated list of employees. Query params: `limit` (default 20), `offset` (default 0), `department`, `is_active`. |
| `GET` | `/stats/summary` | Total employees, active employees and average salary. |

### Examples

The responses below correspond to the dataset committed in this repository.

```bash
curl "http://127.0.0.1:8000/stats/summary"
```

```json
{
  "total_employees": 1000,
  "active_employees": 852,
  "avg_salary": 4579.02
}
```

```bash
curl "http://127.0.0.1:8000/employees?department=Data&is_active=true&limit=2"
```

```json
{
  "total": 169,
  "limit": 2,
  "offset": 0,
  "filters": { "department": "Data", "is_active": true },
  "data": [
    {
      "employee_id": 2,
      "employee_code": "NW-DAT-0002",
      "alias": "Neo",
      "department": "Data",
      "role": "Data Analyst",
      "seniority": "Senior",
      "salary_usd": 5624,
      "hire_date": "2023-08-30",
      "termination_date": null,
      "city": "Bogotá",
      "country": "CO",
      "performance_score": 4.5,
      "employment_type": "contractor",
      "is_active": true
    },
    {
      "employee_id": 8,
      "employee_code": "NW-DAT-0008",
      "alias": "Atlas",
      "department": "Data",
      "role": "Data Engineer",
      "seniority": "Mid",
      "salary_usd": 3964,
      "hire_date": "2025-10-16",
      "termination_date": null,
      "city": "Santiago",
      "country": "CL",
      "performance_score": 4.0,
      "employment_type": "contractor",
      "is_active": true
    }
  ]
}
```

## Current limitations

- The CSV is read on every request; there is no database or caching.
- No authentication.
- No automated tests yet.
