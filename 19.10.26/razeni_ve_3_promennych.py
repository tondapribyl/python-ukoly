a = int(input("Zadej číslo a: "))
b = int(input("Zadej číslo b: "))
c = int(input("Zadej číslo c: "))

if a > b:
    p = a
    a = b
    b = p
if b > c:
    p = b
    b = c
    c = p
if a > b:
    p = a
    a = b
    b = p

print(f"Seřazená čísla: {a}, {b}, {c}")
print(f"Největší číslo je: {c}")
print(f"Nejmenší číslo je: {a}")