#příkaz větvení
x = 0
a = x

if x > 0:
    print("Kladné")
else:
    if (x<0):
        print("Záporné")   
        a = -x
    else:
        print("Nula")
# sem směrují skoky ze všech větví příkazu if

print(f"Absolutní hodnota čísla {x} je {a}")
