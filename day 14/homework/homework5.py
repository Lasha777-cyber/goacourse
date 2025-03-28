names = []

for i in range(5):
    name = input("Please enter a number: ")
    names.append(name)


for name in names:
    if len(name) > 5:
        print('the name consists of more than five letters')
    else:
        print('the name does not consists of more than five letters')