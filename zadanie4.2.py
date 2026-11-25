liczba_produktow = int(input("Podaj liczbe produktow: "))
produkty = []
ceny = []

for i in range(liczba_produktow):
    produkt = input(f"Produkt {i+1}: ")
    cena = float(input("Cena: "))
    produkty.append(produkt)
    ceny.append(cena)

print("\n=== PONUMEROWANA LISTA ===")
for numer, produkt in enumerate(produkty, start=1):
    print(f"{numer}. {produkt}")

print("\n=== CENNIK ===")
for produkt, cena in zip(produkty, ceny):
    print(f"{produkt} - {cena} zl")

suma_cen = sum(ceny)
najwyzsza_cena = max(ceny)
indeks_max = ceny.index(najwyzsza_cena)
najdrozszy_produkt = produkty[indeks_max]

print(f"Suma cen: {suma_cen} zl")
print(f"Najdrozszy produkt: {najdrozszy_produkt} - {najwyzsza_cena} zl")