print("========================================")
print("  Uhodnu tvé číslo! (Mysli si 1 až 100)")
print("========================================")
print("Odpovídej prosím malými písmeny:")
print("  'v' -> pokud je tvé číslo VĚTŠÍ")
print("  'm' -> pokud je tvé číslo MENŠÍ")
print("  's' -> pokud je tip SPRÁVNĚ\n")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy = pokusy + 1
    
    print("Můj tip je:", tip)
    odpoved = input("Odpověď (v / m / s): ")
    
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print("Skvělé! Uhodl jsem tvoje číslo na", pokusy, "pokus.")
    else:
        print("Neplatná odpověď! Zadej prosím 'v', 'm' nebo 's'.")
        pokusy = pokusy - 1