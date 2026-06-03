import re

text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence.
He was born on 23 June 1912 in Maida Vale, London'''

res = re.search("computer", text)
print("Match Object =", res)
print("=" * 79)

# group()
print("group() =", res.group())
print("=" * 79)

# start()
print("start() =", res.start())
print("=" * 79)

# end()
print("end() =", res.end())
print("=" * 79)

# span()
print("span() =", res.span())
print("=" * 79)

# string
print("string =", res.string)
print("=" * 79)

# re
print("re =", res.re)
print("=" * 79)

# pos
print("pos =", res.pos)
print("=" * 79)

# endpos
print("endpos =", res.endpos)
print("=" * 79)

text1=r'search \\ in this string'
res=re.search(r"\\",text1)
print("with r as prefix=",res)
