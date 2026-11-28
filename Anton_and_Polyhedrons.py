def shapes(n):
    sum = 0
    for _ in range(n):
        s = input()
        if s == "Tetrahedron":
            sum += 4
        elif s == "Cube":
            sum += 6
        elif s == "Octahedron":
            sum += 8
        elif s == "Dodecahedron":
            sum += 12
        else:
            sum += 20
    return sum

def main():
    n = int(input())
    print(shapes(n))

if __name__ == "__main__":
    main()