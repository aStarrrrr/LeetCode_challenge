ip_string = str(input("Enter string - ").upper())
rev_string = ip_string[::-1]
if ip_string == rev_string:
    print("Palindrome")
else:
    print("Not Plaindrome")