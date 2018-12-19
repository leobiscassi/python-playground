nome = "henrique"

for c in nome:
    if c in "aeiou":
        print(c.upper())
    elif c == "q":
        print("@")
    else:
        print(c)