people = [
    {"name": "Harry", "house": "Gryffindoe"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Drako", "house": "Slytherin"}
]

# normal way
# def f(person):
#     return person["name"]

# people.sort(key=f)

#Lambda way
people.sort(key=lambda person: person["name"])

print(people)