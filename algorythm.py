
print("Gondolj egy számra 1 és 10 között!")

min = 1
max = 10

answer = "x"

while answer!= "e":
    guess = (min + max) // 2
    print(f"""Erre a számra gondoltam: {guess}""")

    answer = input("Kisebb (k), nagyobb(n) vagy egyenlő(e)?")

    if answer == "k":
        max = guess
    elif answer == "n":
        min = guess
    else:
        print(f"""{guess}-ra gondoltál""")