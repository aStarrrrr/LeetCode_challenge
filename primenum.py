def primeornot(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True
if primeornot(7):
    print("Prime")
else:
    print("not prime")