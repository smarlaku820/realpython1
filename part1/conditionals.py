word = input("Please enter a word:")
length = len(word)

if length < 5:
    print("length of the word is less than 5 characters")
elif length == 5:
    print("length of the word is equal to 5 characters")
else:
    print("length of the word is greater than 5 chracters")