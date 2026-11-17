def anton(n, a):
    counter_A = 0
    counter_B = 0
    counter_C = 0
    for alpha in a:
        if alpha in "A":
            counter_A += 1
        elif alpha in "D":
            counter_B += 1
        else:
            counter_C += 1
    if counter_A == counter_B:
        return "Friendship"
    elif counter_A > counter_B:
        return "Anton"
    else:
        return "Danik"

def main():
    n = int(input())
    a = input()
    print(anton(n, a))

if __name__ == "__main__":
    main()
