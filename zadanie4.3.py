liczba_pomiarow = int(input("Podaj liczbe pomiarow: "))
pomiary = []

for i in range(liczba_pomiarow):
    pomiar = int(input(f"Pomiar {i+1}: "))
    pomiary.append(pomiar)

prog = 50

alarmowe = [x for x in pomiary if x > prog]
podwojone = [x * 2 for x in pomiary]

czy_alarm = any(x > prog for x in pomiary)
czy_wszystkie_ok = all(x <= prog for x in pomiary)

print(f"Pomiary alarmowe: {alarmowe}")
print(f"Pomiary pomnozone przez 2: {podwojone}")
print(f"Czy wystapil alarm? {'Tak' if czy_alarm else 'Nie'}")
print(f"Czy wszystkie pomiary sa prawidlowe? {'Tak' if czy_wszystkie_ok else 'Nie'}")