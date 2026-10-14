# For Loop
print("For Loop:")

for i in range(1, 6):
    print(i)

# While Loop
print("While Loop:")

i = 1
while i <= 5:
    print(i)
    i += 1

# Break
print("Break Example:")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue
print("Continue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# For Loop Else
print("For Loop Else:")

for i in range(1, 4):
    print(i)
else:
    print("Loop completed.")

# While Loop Else
print("While Loop Else:")

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop completed.")

print("Program Finished Successfully!")