def pali(string):
    rev= string[::-1]
    if string.lower() == rev.lower():
        return "palindrome"
    else:
        return "not pal"
print(pali('momjoM'))