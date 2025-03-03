#Arithametic operators

a = 4
k = 40
print(a + k, "->", k - a, "->", a * k, "->", k / a, "->", k // a, "->", a ** k, "->", k % a)

#Relational operators

a = 4
k = 40
print(a < k, "->",a > k, "->",a <= k, "->",a >= k, "->",a == k, "->",a != k)

#Logical operators - and/or/not

#and

# roll_numbers = [1,2,3,4,5,6,7,8,9,10]
# checknum1, checknum2 = map(int,input("And - Enter - ").split(","))
# if checknum1 and checknum2 in roll_numbers:
#     print("Both Accepted")
# else:
#     print("Not Acepted")

#or

# roll_numbers = [1,2,3,4,5,6,7,8,9,10]
# checknum1, checknum2 = map(int,input("Or - Enter - ").split(","))
# if checknum1 or checknum2 in roll_numbers:
#     print("Both Accepted")
# else:
#     print("Not Acepted")

#not

# warnings = [1,2,3,4,5]
# check = int(input("Not - Enter - "))
# if check not in warnings:
#     print("He is decent")
# else:
#     print("Danger")

#is

car = "BMW"
bike = "BMW"
if car is bike:
    print("Same")