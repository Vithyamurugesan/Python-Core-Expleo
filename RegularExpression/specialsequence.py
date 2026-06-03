import re 
text="Alan Turing was born on 23 June 1912 in London"
res=re.findall("\AAlan",text)
print("Result for \A=",res)
print("-"*79)


res = re.findall(r"\bLon", text)
print("Result for \\b =", res)
print("-" * 79)


res = re.findall(r"ring\b", text)
print("Result for \\b =", res)
print("-" * 79)

# \B - Not a word boundary
text1 = "SuperAlanMan"
res = re.findall(r"\BAlan\B", text1)
print("Result for \\B =", res)

print("-" * 79)

# \d - Digits
res = re.findall(r"\d", text)
print("Result for \\d =", res)

print("-" * 79)

# \D - Non-digits
res = re.findall(r"\D", text)
print("Result for \\D =", res[:20])  # first 20 chars

print("-" * 79)

# \s - Whitespace
res = re.findall(r"\s", text)
print("Result for \\s =", res)

print("-" * 79)

# \S - Non-whitespace
res = re.findall(r"\S", text)
print("Result for \\S =", res[:20])  # first 20 chars

print("-" * 79)

# \w - Word characters
res = re.findall(r"\w", text)
print("Result for \\w =", res[:20])  # first 20 chars

print("-" * 79)

# \W - Non-word characters
res = re.findall(r"\W", text)
print("Result for \\W =", res)

print("-" *79)

# \Z - End of string
res = re.findall(r"London\Z", text)
print("Result for \\Z =", res)



