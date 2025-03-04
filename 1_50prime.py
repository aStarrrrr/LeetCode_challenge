def primeornot(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True
out = []
for i in range(1,51):
    if primeornot(i):
        out.append(i)
print(out)