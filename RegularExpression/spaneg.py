import re 
text='''Alan Turing was a pioneer of therotical computer science ans artificial intelligence.He was born on 23 june 1912 in maida vale,London'''
res=re.search('Turing',text)
print("result={} ans start,end position{}".format(res,res.span()))
print(type(res))
