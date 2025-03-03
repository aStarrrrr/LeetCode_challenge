def reverse_string(str):
    out = ""
    for letter in str:
        out = letter + out
    return out
print(reverse_string("Kaattu"))