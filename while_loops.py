# Előtesztelő ciklus:  while ---feltétel--- :  -> amig a while feltétel igaz végrehajtja a törzset, amint a feltétel nem igaz véget ér a ciklus

from mimetypes import guess_all_extensions


number = 0

while number < 10:
    print(number)
    number += 1

print("Innen már nagyobb számok vannak, mint 10")

print("---------------------------------")

number = 1

while number != 0:
    number = int(input("Mondj egy számot!"))
    print(number)
    print("Másikat")

print("Ez 0")

print("---------------------------------")

guess = int(input("Gondolj egy számra 1 és 10 között!"))

min = 1
max = 10

e = 5

while guess != e:
    guess = (min + max) / 2

answer = input("k, n, e")

if answer == "k":
    max = guess
elif answer == "n":
    min = guess
else:
    print("Az 5-re gondoltál")






    


