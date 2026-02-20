# app/salaries.py

import random

SALARY_BY_SENIORITY = {
    "Junior": (1800, 2600),
    "Mid": (2800, 4200),
    "Senior": (4500, 6500),
    "Lead": (6500, 8500),
}

def generate_salary(seniority: str) -> int:
    low, high = SALARY_BY_SENIORITY[seniority]
    return random.randint(low, high)
