# číslo: 1
# číslo: 2
# číslo: 3
# číslo: 4
# číslo: 5

# 1. nastavení počáteční hodnoty řídicí proměnné
pocitadlo = 5

# 2. cyklus běží, dokud platí podmínka (dokud je pocitadlo menší nebo rovno 5)
while pocitadlo > 0 :
    print(f"Číslo: {pocitadlo}")
    pocitadlo -= 1 # Zvýšní hodnoty o 1 (důležité, aby cyklus neskončil v nekonečné smyčce)

print("Konec cyklu")
print(f"Číslo: {pocitadlo}")
