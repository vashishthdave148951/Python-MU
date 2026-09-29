#replacing digits in text 
import re
text_with_digits = "server123 has ip456"
replaced_text = re.sub(r"\d","*",text_with_digits)
print("5. Text after replacement",replaced_text)