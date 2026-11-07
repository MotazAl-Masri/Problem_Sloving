moves = 0
for i in range(5):
    row = list(map(int, input().split()))
    
    if 1 in row:
        
        j = row.index(1)
        
        moves = abs(i - 2) + abs(j - 2)

print(moves)