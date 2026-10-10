dct = {"name": ["sahitya", "aditya" ], "age":[22,22], "city": ["indore","bhopal"]}

naam=dct["name"]
print(naam[0])

naam2 = dct["name"][1] = "sanskar"
print(naam2)


key = dct.keys()
values = dct.values()
print(key)
print(values)


print(dct.get("age"))
print(dct.get("city"))
print(dct.get("name"))
print(dct.items())

dct1 = dct.copy()
print(dct1)

dct1.pop("name")
print(dct1.keys())

dct1.popitem()
print(dct1)

dct1.update({"city": ["indore", "bhopal"]})
print(dct1)

dct.setdefault("name", "pranjay")
print(dct)

print(dct)







