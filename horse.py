def color():
    colors = set(map(int, input().split()))

    remaining_colors = 4 - len(colors)
    
    return remaining_colors
def main():
    print(color())
if __name__ == "__main__":
    main()