counter = 0
n = int(input())
s = input()
for i in range(n):
    if  i < n - 1 and s[i] == s[i + 1] :
        counter += 1
        i += 1
print(counter)