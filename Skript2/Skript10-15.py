# 10. Beschreibe, in kurzen Sätzen, die folgenden imperativen Programmierparadigmen:
# Stukturierte Programmierung, Prozedurale Programmierung, Modulare Programmierung

# Strukturierte: Es beinhaltet zum einen die baumartige Zerlegung eines Programms 
# in Teilprogramme und enthält somit das Paradigma der prozeduralen Programmierung.

# Prozedural: Code ablauf in einer bestimmten Reihenfolge (Von oben nach unten) Prozessor's anfangspunkt
# ist ganz oben (außer es wird abgeändert)

# Modulare Programmierung: Modulare Programmierung ist ein Programmierparadigma. Der Ansatz sieht vor,
#  Computerprogramme systematisch in logische Teilblöcke aufzuspalten
# die Module genannt werden. Modulare Programmierung soll größere Softwareprojekte kontrollierbar und
# übersichtlich halten

# 11. Beschreibe, in kurzen Sätzen, die folgenden deklarativen Programmierparadigmen:
# Funktionale Programmierung, Logische Programmierung
 
# Funktionale: Funktionale Programmierung ist ein Programmierparadigma, in dem Funktionen nicht nur definiert 
# und angewendet werden können, sondern auch wie Daten
#  miteinander verknüpft, als Parameter verwendet und als Funktionsergebnisse auftreten können.

# Logische: Logische Programmierung ist ein Programmierparadigma, das auf der mathematischen Logik beruht.
#  Anders als bei der imperativen 
# Programmierung besteht ein Logik-Programm nicht aus einer Folge von Anweisungen, sondern aus einer Menge 
# von Axiomen, welche hier als eine Ansammlung von Fakten oder Annahmen zu verstehen ist

# 12. Beschreibe, anhand Beispielen, was objektorientierte Programmierung ist.
class Stack():
    """Items habve to be INT"""
    # Create Data Array (List)
    data = []
    # Pop Data (last Index)
    def pop(self):
        return self.data.pop()
    # Push Data 
    def push(self, value: int):
        self.data.append(value)
    # Check if empty
    def CheckEmpty(self):
        if self.data == None:
            return "Stack is empty"
        else: return self.data
# Definiere eine Variable die die Klasse Stack aufruft
c = Stack()
# Rufe Mthoden in C (Stack) auf
c.push(77)
c.push(42)
c.push(55)
print(c.pop())
print(c.CheckEmpty())

# 13. Im Kontext von Python ...
# (a) Was ist das Uberladen von Methoden? Gib 3 Beispiele. ¨
# Bei Python können Operatoren und Standardfunktionen überladen werden, indem man bei einer neuen Klasse 
# bestimmte Methoden mit vorgegebenen Namen definiert. Diese reservierten Methodennamen beginnen und enden
# mit doppelten Unterstrichen.

# (b) Was beschreibt der Begriff ’Shadowing’? Welche Arten von Shadowing existieren in Python? Gib 3 Beispiele.
# Definierte Variablen sind nur in dem bestimmten Kontext erreichbar (ausnahme: global) 
# Wenn  in einer Funktion eine Variable definiert wird kann man diese nur in dieser Funktion benutzen
# Das selbe in Klassen, Methoden und Code der unter dem derzeit auszuführenden Code liegt.

# (c) Beschreibe den Begriff ’Rekursion’. Erstelle 3 Programmbeispiele die iterativ und rekursiv 
# implementierbar sind, und stelle den implementierten Code im Vergleich gegenuber. ¨
# Rekursion: Funktion die sich selbst aufrufen kann
def iterateZahl(zahl):
    for x in range(zahl):
        print(x)
    if zahl != 0:
        iterateZahl(zahl=zahl-1)
iterateZahl(5)

#def AppendText(text):
#    for x in range(len(text)):
#        print(text + str(x))
#    if len(text) < 15:
#        AppendText(text)
#AppendText("meow")


# (d) Was ist Vererbung? Gebe 3 unterschiedliche Beispiele.
# Die Vererbung beschrei bt den Prozess des weitergebens von Daten und methoden an eine andere Klasse um übersicht
# zu behalten 
# Beispiel:
class Katzen():
    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter

class Hunde(Katzen):
    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter)

# (e) Was ist Polymorphismus? Gebe 3 unterschiedliche Beispiele.
# Damit ist die Möglichkeit gemeint, den gleichen Namen für (mehr oder weniger) gleichartige Operationen zu
# verwenden, die auf Objekte unterschiedlicher Klassen 
# angewendet werden. Man spricht auch vom Überladen (overloading) einer Operation.

# (f) Was beschreibt der Begriff ’Datenkapselung’? Gebe 3 Beispiele.
#  Es gibt private Methoden und Variablen innerhalb einer Klasse um das ausversehende ändern von
# Werten zu verhindern

# (g) Was sind Lambda-Funktionen? Gib 3 simple Beispiele wie man eine Lambdafunktion implementieren kann. 
# Eine Lambda funktion ist eine Anonyme Funktion die viele nArgumente nehmen kann aber nur eine Ausgabe gitb.
# Beispiele:
x = lambda a: a + a
print(x(5))

y = lambda a, b: a * b
print(y(2, 100))

z = lambda a, b, c, d, e, f, g: a + b + c + d + e + f + g
print(z(5,5,5,5,5,5,5))

# 14. Was ist ein Design Pattern?
# Pattern sind bestimmte Entwurfsmuster um die art von Programm und den Ablauf darzustellen

# 15. Welche Arten von Design Patterns unterscheidet man voneinander?
# Stuktur pattern, Verhaltensbasiert pattern, Entwurfspattern