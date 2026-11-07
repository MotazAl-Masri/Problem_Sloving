s1 = list(input())
s2 = []
s1.sort()
for i in range(len(s1)):
    if s1[i] == '1' or s1[i] == '2' or s1[i] == '3':
        s2.append(s1[i])
        s2.append('+')

s2.pop()
print("".join(s2))

