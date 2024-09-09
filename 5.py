string = input("")
stringcopy = string
k = int(1)
for i in string:
    print(stringcopy[-k], end="")
    k += 1