s = input().lower()
res = ""

for char in s:
    if char not in "aoyeui":
        res += "." + char

print(res)