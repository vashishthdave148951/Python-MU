import re
sentence = "Python programming is Fun"

capital_words = re.findall(r"\b[A-Z][a-z]*\b", sentence)
print("4. Capitalized Words:")
print(capital_words)