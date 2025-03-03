dict1 = {
    "Name": "Abhinand",
    "Age": "20"
}
dict2 = {
    "Peru": "Kaattu",
    "Vayassu": "21"
}
out = {**dict1, **dict2}
print(out)
print(dict1)
print(dict2)