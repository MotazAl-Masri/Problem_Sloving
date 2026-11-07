w = []
n = int(input())
for i in range(n):
    w.append(input())
for i in range(n):
    if len(w[i]) > 10:
        print(w[i][0] + str(len(w[i]) - 2) + w[i][-1])
    else:
        print(w[i])
        