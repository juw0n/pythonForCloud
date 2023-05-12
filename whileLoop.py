print("Normal while loop Statement")
i = 0
while i < 10:
    print(i)
    i+=1

print("\nBreak while loop Statement")
i = 0
while i < 10:
    print(i)
    if i == 7:
        break
    i+=1

print("\nContinue while loop Statement")
i = 0
while i < 15:
    i+=1
    if i < 9:
        continue
    print(i)

print("\nElse while loop Statement")
i = 0
while i < 20:
    print(i)
    i+=1
else:
    print("i is no longer less than 20")