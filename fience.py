a,b = map(int,input().split())
counter = 0
c = list(map(int,input().split()))
for i in c:
    if i > b:
        counter += 2
    else:
        counter += 1
print(counter)