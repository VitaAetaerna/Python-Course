import random
# 6. Was ist eine Schleife? Erstelle eine Schleife fur folgende Problemstellungen. ¨
# Eine Schleife ist ein wiederholender Code Snippet der unter einer bestimmten bedingung abläuft 

# (a) Die Fibonacci-Reihe ist eine Folge von Zahlen, bei der das n¨achstgr¨oßere Element die Summe der
# jetzigen Zahl und der vorherigen Zahl ist: 1, 1, 2, 3, 5, 8, 13. Programmiere eine Schleife, welche die
# x-te Fibonacci-Zahl berechnet. x ist eine ganze Zahl und wird vom Nutzer eingegeben.
Fibonacci = []
number = 2
numberbehind = 1
for x in range(15):
    tmp = number
    number += numberbehind
    numberbehind = tmp
    Fibonacci.append(number)
print(Fibonacci)
# (b) Die Multiplikation ist das wiederholte addieren von Zahlen. Stelle die Multiplikation von 2 Zahlen
# als Addition, mithilfe einer Schleife da.
a = random.randint(5, 15)
b = random.randint(5, 10)
c = a
print("Zahl 1: ", a, "Zahl 2:", b)
for x in range(b-1):
    a += c
print(a)
# (c) Die Division ist das wiederholte subtrahieren von Zahlen. Stelle die Division von 2 Zahlen als
# Subtraktion, mithilfe einer Schleife da.
dividend = random.randint(15, 40)
divisor = random.randint(1, 10)
quotient = 0
print("Zahl 1: ", dividend, "Zahl 2:", divisor)
while dividend >= divisor:
    dividend -= divisor
    quotient += 1
print(quotient)
# (d) Fur eine beliebige Zeichenkette, suche mithilfe einer Schleife ob der Buchstabe ’a’ vorkommt. Wenn ¨
# ja, gib die Position des ersten ’a’ aus und terminiere die Schleife.
stringToSearch = "Mein Name ist Leon, Hallo"
for lengthOfString in range(len(stringToSearch)):
    if stringToSearch.index("a"):
        print("a was found at ",stringToSearch.index("a"))
        break
    print("\n")


# (e) Fur eine beliebige Zeichenkette, suche mithilfe einer Schleife ob der Buch
# Fur eine beliebige Zeichenkette, suche mithilfe einer Schleife ob der Buchstabe ’a’ oder ’A’ vor- ¨
# kommt. Wenn ja, gib die Position aus und fuhre den Task weiter fort
text = 'Mein Name ist Leon, Hallo a      a     a'
index = 0
while index < len(text):
        index = text.find('a', index)
        if index == -1:
            break
        print('a found at', index)
        index += 1 # +1 because len('a') == 1