thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020
}

thisdict["color"] = "red"
print(thisdict)
thisdict["color"] = "blue"
print(thisdict)
thisdict.update({"name": "jane"})
print(thisdict)

# print(thisdict["asghar"])
print(thisdict.get("asghar"))
print(thisdict.get("asghar", "gashtam nabood nagard nist"))

del thisdict["brand"]
print(thisdict)