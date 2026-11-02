import random
tajne_cislo = random.randint(1,20)

tip = 0
pokusy = 0
max_pokusy = 5

print(f"Myslím si číslo od 1 do 20. Hádej mé číslo! Máš na to {max_pokusy} pokusů.")

while tip!=tajne_cislo and pokusy<max_pokusy:
    tip = int(input("Zadej svůj tip: "))
    if tip<1 or tip>20:
        print("Zadal jsi číslo mimo rozsah (1–20)!")
        continue

    pokusy += 1
    if tip<tajne_cislo:
        print("Moje číslo je větší!")
    elif tip>tajne_cislo:
        print("Moje číslo je menší!")

if tip == tajne_cislo:
    print(f"Gratuluji, uhádl jsi moje číslo {tajne_cislo} na {pokusy} pokusů! :D")
else:
    print(f"Bohužel, nemáš žádné zbývající pokusy. Myslel jsem si číslo {tajne_cislo}.")