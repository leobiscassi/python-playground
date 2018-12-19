nome = "henrique"

print(nome, len(nome))

i = 0

while i < len(nome):
    print(nome[i])
    i += 1

print("\n")

for i in range(len(nome)):
    print(nome[i])

print("\n")

for c in nome:
    print(c)

print("\n")

for i, c in enumerate(nome):
    print(i, c)

print("\n")

for i, c in enumerate(nome):
    if c == "e":
        continue
    print(i, c)

print("\n")

for i, c in enumerate(nome):
    if c == "e":
        break
    print(i, c)

