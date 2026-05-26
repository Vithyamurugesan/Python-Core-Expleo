# Using rfind() method
str1 = input("Enter the string : ")
word = input("Enter the word in that string : ")
position = str1.rfind(word)
print("Last occurrence of", word, "starts at index", position)


'''
Using the for loop
str1=input("enter the string :")
word=input("enter the word in the string :")
last_pos=-1
for i in range(len(str1)):
    if str1[i:i+len(word)]==word:
        last_pos=i
print("Last occurance starts at index",last_pos)

'''
