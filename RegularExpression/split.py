import re 
text='''Alan Turing was a pioneer of therotical computer science ans artificial intelligence.He was born on 23 june 1912 in maida vale,London'''
res=re.split('a',text)
print("Result={}" .format(res))
print(type(res))
