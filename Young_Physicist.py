n = int(input())
sum_x = 0
sum_y = 0
sum_z = 0
for i in range(n):
    a, b, c = map(int, input().split())
    sum_x += a
    sum_y += b
    sum_z += c

if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")