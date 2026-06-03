import re 
text='''Alan Turing was a pioneer of therotical computer science ans artificial intelligence.He was born on 23 june 1912 in maida vale,London'''
res=re.findall('Turing',text)
print("result={}".format(res))
print(type(res))
