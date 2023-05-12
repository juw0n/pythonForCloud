print("Normal for loop Statement")
colours=["Red", "Blue", "Orange", "Yellow", "White", "Black"]
print('Iteration a colours list:')
for x in colours:
    print(x)

print("\nBreak for loop Statement")
colours=["Red", "Blue", "Orange", "Yellow", "White", "Black"]
for x in colours:
    if (x=="Orange"):
        break
    print(x)

print("\nContinue for loop Statement")
colours=["Red", "Blue", "Orange", "Yellow", "White", "Black"]
for x in colours:
    if (x=="Orange"):
        continue
    print(x)

print("\nElse for loop block Statement")
colours=["Red", "Blue", "Orange", "Yellow", "White", "Black"]
for x in colours:
    print(x)
else:
    print("All item have been iterated over")

print("\nRange for loop Statement")
colours=["Red", "Blue", "Orange", "Yellow", "White", "Black"]
for x in range(15):
    print(x)
