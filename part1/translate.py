user_input=input("Enter some text here:")
l = ['a', 'b', 'e', 'l', 'o', 's', 't']
v = [4, 8, 3, 1, 0, 5, 7]
for x in zip(l, v):
    user_input = user_input.replace(x[0], str(x[1]))
print(user_input)