import time, random
# 21. Beschreibe anhand von 3 graphischen Beispielen wie Landau-Symbole funktionieren.

# 22. Was ist eine Datenstruktur?
# Eine Datenstruktur ist ein Komplexer Datentyp der mehrere Variablen (ausnahme kann bestehen) speichern
# kann. 
# 23. Welche Arten von Datenstrukturen gibt es? Welche Komplexit¨aten weisen diese auf fur das auslesen
# und einfugen von Daten? ¨
#  Array (In python Liste), linked list (not a python standard), tuple, list, set, dictionary 
Array = [1,2,3]
Array.append(4) # Fügt 4 hinzu
Array.pop() # Nimmt letzten eintrag (4)

Tuple = (800, 600)
# Tuples können nicht verändert oder gelöscht oder getauscht werden

Set = set()
Set.add(2)
Set.add(4)
Set.pop() #  Nimmt letzten eintrag (4)
Set.clear()

# 24. Implementiere die Ubungen des Python-Codelabs: Stack, Queue, Hashtable, Graph, Tree, Heap

# STACK
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
stack = Stack()
# Rufe Mthoden in C (Stack) auf
stack.push(77)
stack.push(42)
stack.push(55)
print(stack.pop())
print(stack.CheckEmpty())

# QUEUE
class Queue():
    clients = []
    clientQueue = []

    def GetUsers(self, user) -> str:
        self.clients.append(user)
        print("User added: ", user)

    # Let One Through 
    def PopConnect(self) -> str:
        print("Connect user (Popping it out): ", self.clientQueue[len(self.clientQueue)-1])
        self.clientQueue.pop(),
        print(self.clientQueue)
    
    def FillQueue(self):
        if self.clientQueue != 0 and len(self.clientQueue) >= 5:
            self.clientQueue.append(self.clients[len(self.clients[0])])
            print("User added to Queue ", self.client[0])
            self.clients.pop(0)
        else:
           for x in range(len(self.clients)-1):
                self.clientQueue.append(self.clients[x])
                if len(self.clientQueue) >= 5:
                    break
        for x in range(len(self.clients)-2):   
            self.clients.pop(0)

        print("Clients Queue: ", self.clients)
        print("Clients in Queue: ", self.clientQueue)


users = ["Tom", "LeonS", "Irnes", "Chris", "LeonG", "Alex", "Patrick"]

queue = Queue()
for x in range(len(users)):
    queue.GetUsers(users[x])
time.sleep(1)
queue.FillQueue()
queue.PopConnect()
queue.FillQueue()

# 25. Was ist ein Sortieralgorithmus?
# Sortieralgorithmen sind mathematische prozesse die das Sortieren von bestimmten Werten
# in einer Datenstruktur vereinfachen und schneller machen bsp: Brick, Bubble, Quicksort, usw...