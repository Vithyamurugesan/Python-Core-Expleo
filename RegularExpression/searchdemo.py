import re 
text='''Alan Turing was a pioneer of therotical computer science ans artificial intelligence.He was born on 23 june 1912 in maida vale,London'''
res=re.search("^Alan.*London$",text)
if(res):
    print("we have the match")
else:
    print("We don't have the match")
print(type(res))
