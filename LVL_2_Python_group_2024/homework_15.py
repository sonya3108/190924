import json

def add(a, b):
    """Додавання двох чисел"""
    return a + b

def subtract(a, b):
    """Віднімання другого числа від першого"""
    return a - b

def multiply(a, b):
    """Множення двох чисел"""
    return a * b

def divide(a, b):
    """Ділення першого числа на друге (якщо друге не дорівнює нулю)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Піднесення першого числа до степеня другого"""
    return a ** b

def modulus(a, b):
    """Залишок від ділення першого числа на друге"""
    return a % b

def square_root(a):
    """Обчислення квадратного кореня числа"""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return a ** 0.5

def perform_operation(operation, *args):
    """Виконання обраної операції та збереження її в історії"""
    if operation == "add":
        result = add(*args)
    elif operation == "subtract":
        result = subtract(*args)
    elif operation == "multiply":
        result = multiply(*args)
    elif operation == "divide":
        result = divide(*args)
    elif operation == "power":
        result = power(*args)
    elif operation == "modulus":
        result = modulus(*args)
    elif operation == "square_root":
        result = square_root(*args)
    else:
        raise ValueError("Unknown operation")


    operation_str = f"{args[0]} {operation} {args[1] if len(args) > 1 else ''}".strip()
    history[operation_str] = result
    return result

def save_history(filename):
    """Зберігає історію обчислень у файл JSON"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def load_history(filename):
    """Завантажує історію обчислень із файлу JSON"""
    global history
    with open(filename, 'r', encoding='utf-8') as file:
        history = json.load(file)

def sum_first_n_results(n):
    """Повертає суму перших n результатів із історії"""
    values = list(history.values())
    return sum(values[:n])


history = {}


perform_operation("add", 9, 20)
perform_operation("subtract", 16, 0)
perform_operation("multiply", 8, 123)
perform_operation("divide", 200, 45)
perform_operation("power", 23, 3)
perform_operation("modulus", 101, 34)
perform_operation("square_root", 16)


save_history("calculator_history.json")


load_history("calculator_history.json")


sum_of_first_5 = sum_first_n_results(5)
print("Сума перших 5 результатів:", sum_of_first_5)
