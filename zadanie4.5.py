def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Blad: Nie mozna dzielic przez zero!"
    return a / b

def potegowanie(a, b):
    return a ** b

def srednia(liczby):
    if len(liczby) == 0:
        return 0
    return sum(liczby) / len(liczby)

def wyswietl_menu():
    print("\n1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia")
    print("0. Zakoncz")

def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcje: ")
        
        if wybor == '0':
            break
            
        elif wybor in ['1', '2', '3', '4', '5']:
            a = float(input("Podaj pierwsza liczbe: "))
            b = float(input("Podaj druga liczbe: "))
            
            if wybor == '1': print(f"Wynik: {dodawanie(a, b)}")
            elif wybor == '2': print(f"Wynik: {odejmowanie(a, b)}")
            elif wybor == '3': print(f"Wynik: {mnozenie(a, b)}")
            elif wybor == '4': print(f"Wynik: {dzielenie(a, b)}")
            elif wybor == '5': print(f"Wynik: {potegowanie(a, b)}")
            
        elif wybor == '6':
            ile = int(input("Ile liczb chcesz podac? "))
            liczby = []
            for i in range(ile):
                liczba = float(input(f"Liczba {i+1}: "))
                liczby.append(liczba)
            print(f"Srednia: {srednia(liczby)}")
        else:
            print("Nieprawidlowy wybor.")

if __name__ == "__main__":
    main()