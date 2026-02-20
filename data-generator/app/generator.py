# app/generator.py

import random
from faker import Faker

from app.config import (
    COMPANY_PREFIX, DEPARTMENTS, CITIES,
    SENIORITY_LEVELS, EMPLOYMENT_TYPES
)
from app.aliases import generate_alias
from app.salaries import generate_salary
from app.dates import random_hire_date, maybe_termination_date

fake = Faker()

def generate_employee(index: int) -> dict:
    department = random.choice(list(DEPARTMENTS.keys()))
    role = random.choice(DEPARTMENTS[department])
    seniority = random.choice(SENIORITY_LEVELS)
    salary = generate_salary(seniority)

    hire_date = random_hire_date()
    termination_date = maybe_termination_date(hire_date)

    city, country = random.choice(CITIES)

    is_active = termination_date is None

    return {
        "employee_id": index,
        "employee_code": f"{COMPANY_PREFIX}-{department[:3].upper()}-{str(index).zfill(4)}",
        "alias": generate_alias(index),
        "department": department,
        "role": role,
        "seniority": seniority,
        "salary_usd": salary,
        "hire_date": hire_date,
        "termination_date": termination_date,
        "city": city,
        "country": country,
        "performance_score": round(random.uniform(2.5, 5.0), 1),
        "employment_type": random.choice(EMPLOYMENT_TYPES),
        "is_active": is_active,
    }
