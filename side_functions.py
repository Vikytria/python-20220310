import numbers


def delete_middle_element(elements):
    del elements[len(elements) // 2]

numbers = [1, 2, 3, 4, 5, 6]

delete_middle_element(numbers)
print(numbers)

numbers2 = (1, 2, 3, 4, 5, 6)      #nem modosíthato, mert tuple -> hibara fut
delete_middle_element(numbers2)
print(numbers2)