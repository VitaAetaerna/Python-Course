import random 
#Was ist eine Kondition? Welche Formen von Konditionen sind dir bekannt? L¨ose folgende Problemstellungen mithilfe einer Kondition.
# Eine Kondition ist eine Bedingung, diese kann wahr oder Falsch sein und wird in der Programmierung 
# Häufig benutzt 
# Formen der Kondition: If, while Tre/False, while do, do while, switch / case


#(a) Fur eine Zahl A, gib ”positiv” aus wenn die Zahl positiv ist. Gib ”negativ” aus, wenn die Zahl ¨
#negativ ist. Andernfalls, wenn die Zahl 0 ist, gib ”null” aus.
a = random.randint(-5, 5)
print(a)
if a > 0:
    print("Zahl ist positiv")
if a < 0:
    print("Zahl ist negativ")
if a == 0:
    print("Zahl ist 0")

#(b) Wenn A gleich B, dann setze C gleich 5.
a = random.randint(0,2)
b = random.randint(0,2)
c = 0
if a == b:
    c = 5
    print(c)

#(c) Wenn nicht A ungleich B, dann multipliziere C mit D.
a = random.randint(0,2)
b = random.randint(0,2)
c = random.randint(0, 10)
d = random.randint(0, 10)
if not a != b:
    print(c * d)
print("End of Example \n")

#(d) Wenn A den Buchstaben ’e’ beinhaltet, setze B gleich ’Ja’, andernfalls ’Nein’.
A = "Gadse streicheln"
B = False
if "e" in A:
    B = True
    print("Gadse gestreichelt")
print("End of Example \n")

#(e) Wenn A die Zeichenkette ’rot’ beinhaltet, setze B gleich ’Ja’, andernfalls ’Nein’
A = "Rote Gadse ist böse Gadse"
B = False
if "Rot" in A:
    B = True
    print("Alle Gadse gute Gadse")
print("End of Example \n")
