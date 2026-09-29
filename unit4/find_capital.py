import re
sentence = "Python programming is Fun"

capital_words = re.findall(r"[A-Z][a-z]*\b", sentence)
print("4. Capitalized Words:")
print(capital_words)