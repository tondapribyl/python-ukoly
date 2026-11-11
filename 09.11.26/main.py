
# 1. načtení vstupu
n = int(input("Zadej celé číslo k testování: "))

# 2. proměnná pro uchování výsledku (tzv. stavová proměnná)
je_prvocislo = True

# 3. ošetření čísel menších než 2
if n < 2:
    je_prvocislo = False
else:
    # 4. naivní cyklus WHILE (zkoušíme všechna čísla od 2 do n-1)
    i = 2
    while i < n:
        if n % i == 0:
            je_prvocislo = False  # našli jsme dělitele, není to prvočíslo
            break                 # hned ukončíme cyklus
        i += 1                    # posun na další číslo (+1)

# 5. Výpis výsledku
if je_prvocislo:
    print(f"Číslo {n} JE prvočíslo.")
else:
    print(f"Číslo {n} NENÍ prvočíslo.")

 