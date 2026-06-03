import re 
text='''Alan Turing was a pioneer of therotical computer science and therotical artificial intelligence.He was born on 23 june 1912 in maida vale,London'''
res=re.sub('therotical','practical',text)
print("Result={}" .format(res))
print(type(res))
