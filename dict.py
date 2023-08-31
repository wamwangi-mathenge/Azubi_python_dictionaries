tel = {
    "P. McCartney": 123456,
    "J. Lennon": 987654,
    "G. Harrison": 113425,
    "R. Starr": 777888
}

print(tel)
print(tel["G. Harrison"])
print(tel["P. McCartney"])


## Adding key-value pairs to a dictionary
tel["Y. Ono"] = 546333
tel["B. Epstein"] = 998777

print(tel)

## replacing the value for an existing key
tel["P. McCartney"] = 654321

print(tel)

## Dictionaries of mixed data types
stupid_dict = {
    123: "blablabla",
    True: 123456,
    "key": False,
    (123, "abc"): 1000,
    34.5: [0, 1, 2, 4, 5],
}

print(stupid_dict)

## The key in a dictionary is immutable
new_phone = {
    ("Paul", "McCartney"): 123456
}
print(new_phone)


# new_phone = {
#     ["Paul", "McCartney"]: 123456
# }

# print(new_phone)

## Deleting an element
del tel["P. McCartney"]
print(tel)

## Iterating over a dictionary with a for loop
for name in tel:
    print(name, tel[name])
    

## General functions and methods
print(len(tel))
print(tel.keys())
print(tel.values())
print(tel.items())