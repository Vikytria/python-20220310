#  Megjegyzés :D

print(5)
print(500_000)               #  csak a kódban látszik, olvasást segíti a
print("Hello World!")
print('Hello world')
print('Hello "World"')
print(True)
print(False)

print(type(5))                #  Konstans adattypus kiiratása
print(type(5.2))
print(type("Hello World!"))
print(type('Hello World!'))
print(type(True))
print(type(False))

print("""Több soros string,
        Még egy sor""")

greetings = "Jó reggelt!"
print(greetings)
greetings = "Jó estét!"
print(greetings)

print(type(greetings))

#Feladat
wheel_of_car = 4
print(type(wheel_of_car))
pi = 3.14
print(type(pi))

houses = 12
print(houses)
print(type(houses))
houses = "Sok"
print(houses)
print(type(houses))

#  type hint -> meg lehet adni hogy milyen típusú értéket kellene megadni a változonak
number_of_cars: int = 16

number_of_cars_in_parking = number_of_cars
print(number_of_cars_in_parking)

number_of_cars_in_parking = 20
print(number_of_cars_in_parking)
print(number_of_cars)

print(len("alma"))
length_of_apple = len("alma")
print(length_of_apple)

#  Operátorok

print(10 + 3)
print(20 - 4)
print(5 * 4)
print(5.4 * 7.4)
print(10 / 6)
print(6.5 - 4)             #  csunya kerekítés a vége, mert a tizedesek bináris számrendszerben nem ábrázolhatóak - kerekíteni kell
print(10.6 - 10.0)
print(30 % 7)

name = "John Doe"
age = 40

print(name, age, "éves")

print(name, age, "éves", sep="****")   # sep: a megdott változok között milyen elválasztás van
print(name + " " + str(age) + " éves")

print("Hello" + "World")
fruit1 = "alma"
fruit2 = "körte"
print(fruit1 + fruit2)

print(f"A {name} emberke {age} eves")  # string interpolation
print(f"A 3 + 5 kifejezés értéke: {3 + 5}")  # string interpolation


