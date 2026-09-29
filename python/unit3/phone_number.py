import re
phone = "9874563214"

if re.match(r"\d{10}",phone):
    print("3. Valid Phone Number")
else:
    print("3. Invalid Phone Number")