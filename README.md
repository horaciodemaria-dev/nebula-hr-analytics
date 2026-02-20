# Nebula HR Analytics

FastAPI-based HR analytics backend plus a synthetic employee data generator.

## Structure

- `backend/`: API service and dataset consumed by the API
- `data-generator/`: script and modules to generate synthetic employee data

## 1) Generate synthetic data

From project root:

```bash
cd data-generator
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generate.py
```

This creates/updates `data-generator/employees.csv`.

## 2) Run the API

From project root:

```bash
cd backend
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API base URL: `http://127.0.0.1:8000`

## Main endpoints

- `GET /`
- `GET /employees`
- `GET /stats/summary`

Example filters:

- `/employees?limit=20&offset=0`
- `/employees?department=Engineering`
- `/employees?is_active=true`
