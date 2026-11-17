a = input()

counter = 0

for digit in a:
    if digit in "47":
        counter += 1

if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")