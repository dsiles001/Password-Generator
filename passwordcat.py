import itertools

words = input("Enter 10 or more words to be used: ")
limits = input("How long do you want your generated passwords to be: (MIN MAX): ").split()

for i in range(len(limits)):
    limits[i] = int(limits[i])



words = words.split()

# possiblecombos = []
with open('passwords.txt', 'w') as file:
    for i in range(1,len(words)+1):
        for combo in itertools.product(words, repeat = i):
            combo = ''.join(combo)
            if limits[0] <= len(combo) < limits[1]:
                file.write(f"{combo}\n")
            else:
                continue
    
print("finished")