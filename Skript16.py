import random
# 16. Erstelle ein theoretisches Konzept zur Problemlösung folgender Probleme. Modelliere kurz, wie sich ein
# Programm implementieren liese (graphisch, Pseudocode, ...). Implementiere anschließend eine ausführbare 
# Lösung in Python.

# (a) Fur eine ganze Dezimalzahl A, gebe die Zahl A in Binärformat aus.
# Beispiel: 2210 - 101102

#                                                    Pseudocode
#                                                    
#                                                    DZahl = 64
#                                                    for x in länge(DZahl)
#                                                        DZahl : 2 // Rest weglegen
#                                                        Wenn Zahl 0 ist: Stop
#                                                    print(Binärzahl als Array)


def BinaryConv(number):
    rest = []
    length = 0
    if number < 256:
        length = 8
    elif number > 256 and number < 65536:
        length = 16
    for x in range(length):
        rest.append(number % 2)
        number = number // 2

    return rest[::-1]


BNumber = str(BinaryConv(random.randint(1, 65536)))
BNumber = BNumber.replace(",", "")
BNumber = BNumber.replace(" ", "")
BNumber = BNumber.replace("[", "")
BNumber = BNumber.replace("]", "")
print("Binary: ", BNumber)
print("End of Example \n")


# (b) Fur eine ganze Dezimalzahl A, gebe die Zahl A in Oktalformat aus. Nutze hierzu nicht den Print-
# spezifizierer ”%o”.
# Beispiel: 2210 - 268
#                                                    Pseudocode
#                                                    
#                                                    DZahl = 64
#                                                    for x in länge(DZahl)
#                                                        DZahl : 8 // Rest weglegen
#                                                        Wenn Zahl 0 ist: Stop
#                                                    print(Oktalzahl als Array)
def OctalConv(decNumber):
    octalrest = []
    while decNumber:
        octalrest.append(decNumber % 8)
        decNumber = decNumber // 8

    return octalrest[::-1]


octalNumber = str(OctalConv(260))
octalNumber = octalNumber.replace(",", "")
octalNumber = octalNumber.replace(" ", "")
octalNumber = octalNumber.replace("[", "")
octalNumber = octalNumber.replace("]", "")
print("Octal: ", octalNumber)
print("End of Example \n")

# (c) Fur eine ganze Dezimalzahl A, gebe die Zahl A in Hexadezimalformat aus. Nutze hierzu nicht den ¨
# Printspezifizierer ”%x”.
# Beispiel: 2210 - 1616
#                                                    Pseudocode
#                                                    
#                                                    DZahl = 64
#                                                    for x in länge(DZahl)
#                                                        DZahl : 16 // Rest weglegen
#                                                        Wenn Zahl 0 ist: Stop
#                                                    print(Hexazahl als Array)
def HexConv(decNumber):
    HexRest = []
    while decNumber:
        if decNumber % 16 >= 10:
            if decNumber % 16 == 10:
                HexRest.append("A")
            elif decNumber % 16 == 11:
                HexRest.append("B")
            elif decNumber % 16 == 12:
                HexRest.append("c")
            elif decNumber % 16 == 13:
                HexRest.append("D")
            elif decNumber % 16 == 14:
                HexRest.append("E")
            elif decNumber % 16 == 15:
                HexRest.append("F")
        elif decNumber % 16 < 10:
            HexRest.append(decNumber % 16)
        decNumber = decNumber // 16
    return HexRest[::-1]


hexNumber = str(HexConv(724))
hexNumber = hexNumber.replace(",", "")
hexNumber = hexNumber.replace(" ", "")
hexNumber = hexNumber.replace("[", "")
hexNumber = hexNumber.replace("]", "")
hexNumber = hexNumber.replace("'", "")
print("Hex: ", hexNumber)
print("End of Example \n")


# (d) Fur eine Zeichenkette A, kontrolliere ob der Inhalt dieser Zeichenkette lexikographisch geordnet ¨
# ist.
def LexikographischArray(array):
    for i in range(len(array)):
        array[i] = str(array[i]).lower()

    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

LexikographischArray(["a", "c", "x", "z", "Q", "E", "S", "b", "f", "p"])
print("End of Example \n")


# (e) Fur ein Array aus ganzen Zahlen A, sortiere die einzelnen Elemente nach Gr ¨ ¨oße. Nutze hierzu eine
# eigene Implementierung uber Schleifen. ¨
# Beispiele fur Sortierung: [0 ¨ , 3, 2, 5, 4] - [0, 2, 3, 4, 5]
def Sort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

Sort([1,9,9,65,3,7,5,3])
print("End of Example \n")


# (f) Wenn A eine Zeichenkette beinhaltet, kontrolliere ob es sich um ein Palidrom handelt. Ein Palidrom
# ist ein Wort das sich von links gleich liest, wie von rechts (vorsicht mit Leerzeichen!). Wenn A ein
# Palidrom ist, dann gebe ’Ja’, andernfalls ’Nein’ aus.
# Beispiele fur Palindrome: ’Ava’, ’Dad’, ’Ebbe’, ’Ehe’, ’Rotor’, ’Der Freibier Fred’, ’Und nu’ ¨
def Palidrom(text):
    text = str(text)
    if text.lower() == text[::-1].lower():
        print("Palidrom")
    else: print("Kein Palidrom")

Palidrom("Anna")
Palidrom("meow")
print("End of Example \n")


# (g) Wenn A und B jweils eine Zeichenkette beinhalten, kontrolliere ob A ein Anagramm von B ist.
# Ein Anagram ist ein Wort, dessen Buchstaben man zu einem anderen Wort umformen kann.
# Beispiele fur Anagramme: ’Lehm’ - ’Mehl’, ’Maus’ - ’Saum’, ’Tom Vorlost Riddle’ - ’Ist Lord ¨
# Voldemort’

# (h) Wenn A eine Zeichenkette beinhaltet, kontrolliere ob es sich um ein Isogramm handelt. Ein Isogramm ist ein Wort oder Satz, in welcher jeder Buchstabe nur einmal, oder gleich h¨aufig, vorkommt.
# Beispiele fur Isogramme: ’Mobilfunkgespr ¨ ¨ach’, ’Heiz¨olruckstoßabd ¨ ¨ampfung’, ’Dorfplatzschießubung’, ¨
# ’Großkatzenimpfbuch’