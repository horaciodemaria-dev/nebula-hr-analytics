# app/dates.py

import random
from datetime import date, timedelta

def random_hire_date():
    start = date(2014, 1, 1)
    end = date.today()
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

def maybe_termination_date(hire_date):
    if random.random() < 0.15:
        min_days = 180
        max_days = 2500
        return hire_date + timedelta(days=random.randint(min_days, max_days))
    return None
