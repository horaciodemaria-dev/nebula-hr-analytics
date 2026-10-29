# Data generator

Generates the synthetic employee dataset used by the API in [`../backend`](../backend).

## Run

```bash
python -m venv venv
source venv/bin/activate          # Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generate.py
```

This writes `employees.csv` in the current folder (1,000 rows by default). The API reads its own copy at `backend/data/employees.csv`, so copy the file there to use the new data:

```bash
cp employees.csv ../backend/data/employees.csv      # Windows: copy employees.csv ..\backend\data\employees.csv
```

## Configuration

Edit `app/config.py` to change:

- `NUM_EMPLOYEES`: how many rows to generate
- `DEPARTMENTS` and their roles
- `CITIES` (city and country code)
- `SENIORITY_LEVELS` and `EMPLOYMENT_TYPES`

Salary ranges per seniority level are in `app/salaries.py`.

## How the data is built

Each row is created in `app/generator.py`: a random department and role, a seniority level with a matching salary range, a hire date between 2014 and today, and a 15% chance of a termination date (`is_active` is false when there is one). The generator is not seeded, so each run gives a different dataset.
