warsztat_python = set()
warsztat_ai = set()

while True:
    print("\n1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyswietl uczestnikow")
    print("4. Uczestnicy obu warsztatow")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakoncz")
    
    opcja = input("Wybierz opcje: ")
    
    if opcja == '1':
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        warsztat_python.add((imie, nazwisko))
        print("Dodano uczestnika.")
        
    elif opcja == '2':
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        warsztat_ai.add((imie, nazwisko))
        print("Dodano uczestnika.")
        
    elif opcja == '3':
        print(f"Python: {sorted(warsztat_python)}")
        print(f"AI: {sorted(warsztat_ai)}")
        
    elif opcja == '4':
        wspolni = warsztat_python & warsztat_ai
        print("Uczestnicy obu warsztatow:")
        for u in sorted(wspolni):
            print(f"{u[0]} {u[1]}")
            
    elif opcja == '5':
        wszyscy = warsztat_python | warsztat_ai
        print("Wszyscy unikalni uczestnicy:")
        for u in sorted(wszyscy):
            print(f"{u[0]} {u[1]}")
            
    elif opcja == '0':
        break
    else:
        print("Nieprawidlowy wybor.")