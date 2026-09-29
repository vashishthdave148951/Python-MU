import re

text = "Cybersecurity Lab 2025"
if re.search(r"\d",text):
    print("1. The string contains a number")
else:
    print("1. No number found in the string")