# 1


factory = {
    "IT department": 50,
    "Sales department": 30,
    "Production department": 100,
    "Law department": 10,
    "Construction department": 20
}


factory["IT department"] = 60


factory["Marketing department"] = 25


del factory["Law department"]


total_employees = sum(factory.values())

print(f"Загальна кількість працівників: {total_employees}")
print("Оновлений словник:", factory)

# 2

import json


def save_to_json(data, filename='factory_data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


save_to_json(factory)


def load_from_json_and_calculate_total(filename='factory_data.json'):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    total_employees = sum(data.values())
    return total_employees


total_employees_json = load_from_json_and_calculate_total()
print(f"Загальна кількість працівників (після читання з JSON): {total_employees_json}")

# 3


import csv


def save_to_csv(data, filename='factory_data.csv'):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Department', 'Employees'])
        for department, employees in data.items():
            writer.writerow([department, employees])


save_to_json(factory)
save_to_csv(factory)


def load_from_csv_and_calculate_total(filename='factory_data.csv'):
    total_employees = 0
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            total_employees += int(row['Employees'])
    return total_employees


total_employees_json = load_from_json_and_calculate_total()
total_employees_csv = load_from_csv_and_calculate_total()

print(f"Загальна кількість працівників (після читання з JSON): {total_employees_json}")
print(f"Загальна кількість працівників (після читання з CSV): {total_employees_csv}")

