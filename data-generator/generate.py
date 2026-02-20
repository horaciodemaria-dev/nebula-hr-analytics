# generate.py

from app.config import NUM_EMPLOYEES
from app.generator import generate_employee
from app.csv_writer import write_csv

def main():
    data = [generate_employee(i + 1) for i in range(NUM_EMPLOYEES)]
    write_csv(data, "employees.csv")
    print(f"Generated {len(data)} employees")

if __name__ == "__main__":
    main()
