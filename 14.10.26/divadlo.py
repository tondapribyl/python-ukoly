
pocet = int(input("Zadej počet osob: "))
cena_osoba = 500

if pocet>=4:
    cena_celkem = cena_osoba * pocet * 0.75         #skupinová slave
else:
    vek = float(input("Zadej věk: "))
    if vek>=65:
        cena_celkem = cena_osoba * pocet * 0.8      #sleva pro seniory
    elif vek<26:
        student = input("Jsi student? (ano/ne)")
        if student=="ano":
            cena_celkem = cena_osoba * pocet * 0.7
        else:
            cena_celkem = cena_osoba * pocet
    else:
     cena_celkem = cena_osoba * pocet

# sem to skočí po vykování všech podmínek
print("Cena vstupenky:", cena_celkem / pocet)
print("Cena celková:", cena_celkem)