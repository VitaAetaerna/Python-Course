import random 

# 8. Wie definiert man eine Funktion in Python? Gibt es eine Main-Funktion?
# Funktionen definiert man mit "def NameDerFunktion():", Es gibt KEINE direkte Main 
# FUnktion aber man kann eine beliebige Funktion erstellen und dann selbst festlegen dass
# dies der Einstiegspunkt dess Programmes bzw. der CPU ist.

# 9.  Erstelle eine Funktion fur folgende Problemstellungen. Setze passende Rückgabewerte für den Caller. ¨
# (a) Erstelle eine Funktion ”sum(a, b, c, d)”, welche die Summe von a,b,c,d zuruckgibt.
def Summe(a,b,c,d,):
    return a+b+c+d
print(Summe(5,4,3,2))
print("End of Example \n")

# (b) Erstelle eine Funktion ”revert(array)”, welche den Inhalt eines Arrays reversiert.
# Beispiel: [2, 4, 6] - [6, 4, 2], ["abc"] - ["cba"]
def Revert(arrayToRevert):
    newLst = arrayToRevert[::-1]
    return newLst
Text = ["meow", "woem", "woof", "foow"]
print(Revert(Text))
print("End of Example \n")
# (c) Erstelle eine Funktion ”trim(array, x, y)’, welche den Inhalt des Arrays von ’x’ bis ’y’ zuruckgibt. ¨
# Beispiel: trim([0, 1, 2, 3, 4], 1, 3) - [1, 2, 3]
def Trim(array, entrance, exit):
    start = array.index(entrance)
    end = array.index(exit)
    for x in range(end - start+1):
        print(array[start+x])
print(Trim([1,2,3,4,5,6,7,8,9], 3, 7))
print("End of Example \n")


# (d) Erstelle eine Funktion ”compare(a,b)”, welche die Elemente auf Wert und Typ kontrolliert. Ist der
# Wert gleich, gib ”Wert ist gleich.” aus. Ist der Typ gleich, gib ”Typ ist gleich.” aus. Sollte beides
# ungleich sein, so gebe ”Werte sind ungleich” aus.

def Compare(a,b):
    if a == b and type(a) == type(b):
        return "Werte und Typen sind gleich"

    if a != b and type(a) != type(b):
        return "Werte und Typen sind ungleich"
    if a == b:
        return "Wert ist gleich"
    if type(a) == type(b):
        return "Typ ist gleich"
    
print(Compare("Hallo", "Hallo"))

# 10. Was beschreibt die ’Big-O Notation’? Was genau versteht man unter dem Begriff Komplexitätt?
# Big O beschreibt die Länge, Größe und Komplexität eines Algorithmus, dann wird der Algorithmus in 
# Komplexitätsstufen bewertet
# Komplexität in der Programmierung ist der Wert den Eine Instanz an Resourcen und Zeit verbraucht