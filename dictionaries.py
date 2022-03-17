# Dictionary -> szótár // adattíípus

# Bal hasáb: kulcs / key   ----  Jobb hasáb: érték / value
# bármilyen adatípus lehet, de a kulcsnak egyedinek kell lennie
# nincsen sorrend benne
# kifejezése = json -> böngészőben is foyltatható

employee = {"name": "John Doe", "age" : 40}
print(employee["name"])

# Szótár bejárása - csak a kulcsok kiiratása
for data in employee:
    print(data)

# szótár bejárása - minden kiratása
for key, value in employee.items(): 
    print(key)
    print(value)
    print(f"{key} --- {value}")

# Szótár módosítása
employee["age"] = 41
print(employee)

# Szótár bővítése
employee["color_of_eye"] = "blue"
print(employee)

employee["skills"] = ("Python", "HTML", "CSS")
print(employee)
print(employee["skills"][1])   # szótárban szereplő lista x. elemének megadása

# Szótárban lévő szótár egyik értékének kiszedése
salaries = {"2021-01": 100_000, "2021-02": 100_500, "2021-03": 150_000}
employee["salaries"] = salaries
print(employee["salaries"]["2021-03"]) 










