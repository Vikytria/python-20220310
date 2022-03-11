# Függvény: utasítások halmaza

def print_employee_data(name: str, birth_date: int, current_year: int):
    print("Name:", name)
    print("Születési év:", birth_date)
    print("Kora:", current_year - birth_date)

def calculated_age(birth_date: int, current_year: int):
    return current_year - birth_date

print_employee_data("John Doe", 1998, 2022)
print_employee_data("Jack Doe", 1996, 2022)
print_employee_data("Jane Doe", 1992, 2022)

print(calculated_age(2012, 2022))

result = calculated_age(2012, 2022)
print(f"A gyerek {result} éves")