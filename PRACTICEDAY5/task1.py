def number_in_words():
    words={
         0:'zero',
         1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine'
    }
    num = input("Enter the values: ").split()
    for i in num:
        i = int(i)
        if i in words.keys():
            print(words[i])
number_in_words()

    


