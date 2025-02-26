#int, float, complex
#Numeric Data Types

a = 40
k = 4

a = 40.4
k = 4.40

ka = 4 + 40j
print(type(ka))
print("---------------------------------------------")

#List, tuple, string, range
#Sequence Data Types and Set Data Types #Set

string = "Kaattu"
print(string)
print("---------------------------------------------")
print(type(string))
print("---------------------------------------------")
tpl = (1,2,3,4,5,6,"key")
print(tpl)
print("---------------------------------------------")
print(type(tpl))
print("---------------------------------------------")
test_list = [1,2,3,4,5,5,4,3,"key"]
print(test_list)
print("---------------------------------------------")
print(*test_list)
print("---------------------------------------------")
removed_duplicates = set(test_list)
print(removed_duplicates)
print("---------------------------------------------")
print(*removed_duplicates)
print("---------------------------------------------")
print(type(removed_duplicates))
print("---------------------------------------------")
r = range(1,100)
print(type(r))
print("---------------------------------------------")
frozen = frozenset(removed_duplicates)
print(type(frozen))
print("---------------------------------------------")

#Dictionary

dict1 = {
    "Name" : "Abhinand Shaji",
    "Age" : 20,
    "Place" : "Kochi"
}
print(dict1)
print("---------------------------------------------")
print(type(dict1))
print("---------------------------------------------")
print(dict1["Name"])
print("---------------------------------------------")
for key in dict1:
    print(f"{key} , {dict1[key]}")
print("---------------------------------------------")
print(*dict1)
print("---------------------------------------------")
for key, value in dict1.items():
    print(f"{key}: {value}")
print("---------------------------------------------")

#Boolean

a = True
b = False
if a == True:
    print("Iam a pro")
    print("---------------------------------------------")
print(a)
print("---------------------------------------------")
print(type(b))
print("---------------------------------------------")