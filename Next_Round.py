n,k =map(int, input().split())
listed = list(map(int, input().split()))

count = 0
for score in listed:
    if score >= listed[k-1] and score > 0:
        count += 1

print(count)