# D E N N Í  P O Z D R A V
#
#noc:           méně než 5
#ráno:          méně než 10
#dopoledne:     méně než 12
#poledne:       přesně 12
#odpoledne:     méně než 17
#večer:         méně než 22
#noc:           více nebo rovno 22

cas = float(input("Zadej čas: "))

if cas<0:
    print("Chybné zadání!")
elif cas<5:
    print("Dobrou noc!")
elif cas<10:
    print("Dobré ráno!")
elif cas<12:
    print("Dobré dopoledne!")
elif cas == 12:
    print("Dobré poledne!")
elif cas<17:
    print("Dobré odpoledne!")
elif cas<22:
    print("Dobrý večer!")
elif cas>=22:
    print("Dobrou noc!")

else:
    print("Chybné zadání!")