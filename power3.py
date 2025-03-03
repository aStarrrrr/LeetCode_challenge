def prw(base, exponent):
    out = 1
    for _ in range(exponent):
        out *= base
    return out
print(prw(4,10))