table = (("Henrique", "Niterói", 22.9, 43.1),
         ("Vinícius", "Santarém", 2.4, 54.7))

for nome, *_ in table:
    print(nome, _)

