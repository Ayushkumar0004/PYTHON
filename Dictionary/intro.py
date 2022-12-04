#Dictionary are ordered
#key and value pair are must
mydictionary = {
    "name":"Ayush",
    "Age":"18",
    "Class":12,
    "percentage":83
}
a = mydictionary.keys()
b = mydictionary.values()
print(a)
print(b)
print(mydictionary.get("Age"))
print((mydictionary))
print(len(mydictionary))
#ordered 
#duplicates are not allowed
mydictionary["Age"] =19
print(mydictionary)
mydictionary.update({"Age":22})
print(mydictionary)
mydictionary.pop("Class")
print(mydictionary)
