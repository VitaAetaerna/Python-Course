import sys
import random 

# Fragen von @ThompsonA93 und @nekosilvertail



# 1. Was ist Python? Wie fuktioniert pythion?
# Python ist eine Objektorientierte oder Prozedurale Programmiersprache die von
# Guido von Rossum in den 90er erstellt wurde.
# Python ist KEINE Compiler Sprache sondern eine Interpretierte Sprache
# Das bedeuted dass das ausgeführte Skript nicht einmal Kompiliert und dann eine
# EXE erstellt wird sondern dass das Skript bei jeder ausführung wieder erneut Interpretiert wird.

# 2. Welche primitiven Datentypen kennt man in Python? Wie werden diese im Speicher angelegt?
# Int, Float, Binär, Hexa, String, Char, 
# Daten werden im Speicher als Zahlen abgelegt, alles was keine Zahl ist wird mittels einer Tabelle z.B.
# ASCII asoziiert und dann damit übersetzt

# 3. Welche komplexen Datentypen bzw. Datenstrukturen kennt man in Python? Wie unterscheiden sich
# diese voneinander?
# List, Tuple, Dictionary, Array
# Diese Unterscheiden sich von der Art wie sie gespeichert werden und was sie Speichern können
# Ein Dict kann zum Beispiel eine Variable speichern auf die man dann mit einem bestimmten 
# Keyword zugreifen kann.
# Ein Array ist eine Anneinanderreihung von Werten (Immer hintereinander im Speicher liegend)

# 4. Was sind Operatoren?
# (a) Definiere die arithmetischen Operatoren anhand eines kurzen Python-Programmes.
a = random.randint(30, 50)
b = random.randint(0, 30)
#Addition
print(a + b)

# Subrtaktion
print(a - b)

# Multiplikation
print(a * b)

#Division
print (a / b)

# Modulo
print(a % b)

# (b) Definiere die bitweisen Operatoren anhand eines kurzen Python-Programmes.
c = random.randint(30, 50)
c = bin(c)
d = random.randint(10, 30)
d = bin(d)

# & und bzw. And
print(c & d)

# | oder bzw. Or
print(c | d)

# ~ negieren bzw. Negation
print(~c, ~b)

# ^ extra oder bzw. XOR
print(c ^ d)

# (c) Definiere die logischen Operatoren anhand eines kurzen Python-Programmes
e = 10
f = 10

# and / Und
print((e==f) and (f==e))

# or / Oder
print((e==f) or (f==7))

# not / Nicht
print(not(e==f))

# Wie funktionieren diese Operatoren, wenn man sie bei komplexen Datentypen einsetzt?
# Sie können gleich funktionieren oder abänderungen enthalten durch die Struktur der Variable

# (a) Wie lassen sich Werte von Sequenzen addieren?

# Liste
print([1,2,3] + [1,2,3])

# Tuple
print((1,2) + (1,2))


# (b) Wie werden Mapping-Daten zusammengefugt?

# (c) Wie kombiniert man Set-Daten?
g = set()
h = set()
g.add("h"), h.add("g")
print(g, h)




