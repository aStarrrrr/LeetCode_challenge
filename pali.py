def palindrome(str):
    out = ""
    for letter in str:
        out = letter + out
    return out
inp = str(input("Enter the string to check: ")).lower()
if inp == palindrome(inp):
    print("Palindrome")
else:
    print("Not Palindrome")
