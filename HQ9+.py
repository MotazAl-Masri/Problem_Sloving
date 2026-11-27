def HQ9(n):
    for char in n:
        if char in "HQ9":  # noqa: SIM103
            return True
    return False
def main():
    n = input()
    if HQ9(n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
