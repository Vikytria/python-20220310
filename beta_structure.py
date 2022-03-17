# Adatszerkezet
    # Egyszerű - int, float
    # Összetett - str, list

# Indexálással kinyerhető egy karakter
fruit = "cseresznye"
print(fruit[2])

# szeletelés = slicing
print(fruit[2:7])     
print(fruit[2:7:2])   # 2től 7ig minden második
print(fruit[2:])      # 2 indextől a végéig
print(fruit[::-1])    # visszafelé írja ki
#print(fruit("*" + fruit[:-3]))   # elejétől kezd + a végérol az utolsó 3at levágja

#műveletek stringgel
print(fruit.upper())   # nagybetűsíti a stringet

#Módosítani a str értékét csak ugy lehet ha a változot újra definiláom másik értékkel
fruit = fruit.upper()
print(fruit)

#ciklussal végig lehet lépkedni a str karakterein
for c in fruit: 
    print(c)

#Karakterhossz
print(len(fruit))

#Összehasonlítás - boolean lesz
print(fruit == "CSERESZNYE")

#Részlet keresése egy strben - boolen lesz
print("ERESZ" in fruit)

#Adott szórészletre végződik-e - boolean lesz
print(fruit.endswith("NYE"))

#Egész számot tartalmaz-e - boolean lesz
print(fruit.isdecimal())

#Random strről eldönteni hogy szám-e
print("1234".isdecimal())

#Spacek levágása
print("       teszt    ".strip())

#Az adott szórészlet hanyadik indexen van
print(fruit.index("RE"))

#Hányadik karaktertől nézzen
print(fruit.index("E", 3))

#Adott karaktereket kicserééljen
print(fruit.replace("E", "X"))

#Az első paraméterekkel elválasztva felsorolja a lista elemeket
print(",".join(["a", "b", "c"]))

#HTML lista szétszeletésle rendes listába
paragraph = "alma korte barack meggy"
fruits = paragraph.split()
print(fruits)
fruits = paragraph.split(",")

#Stringek összefűzése
print(f"A kedvenc gyümülcseim? {fruit}, ennyi van belöle: {len(fruit)}")




