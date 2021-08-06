x = 1

while x < 10:
    print(x)
    x += 1

# Except number 4
print("---")
x = 1
while x < 10:
    if x == 4:
        x += 1
        continue

    print(x)
    x += 1

# It breaks when hits 4
print("---")
x = 1
while x < 10:
    if x == 4:
        x += 1
        break

    print(x)
    x += 1
