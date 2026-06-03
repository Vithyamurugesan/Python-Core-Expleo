import re
pattern = r'\b\w+ing\b'
text = "Walking and taking are importatnt activities"
#match_result=re.search(pattern,text)
match_result = re.findall(pattern, text)
if match_result:
   # print("match found",match_result.group())
     print("match found",match_result)
else:
    print("no match found")
print(match_result)
