import re
text = input("Cyber Security Lab 2025")
if re.search(r"\d", text):
    print("2. The string contains a number")
else:
    print("2. No number found in the string")