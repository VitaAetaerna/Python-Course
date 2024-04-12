import random
# 28. Was ist ein Suchalgorithmus?
# Ein suchalgorithmus ist ein Mathematischer Prozess der das suchen  von Objekten in einer Liste
# verschnellert und erleichtert. Auch diese kann man paralellisyrien

# 29. . Implementiere die Ubungen des Python-Codelabs: LinearSearch, BinarySearch, InterpolationSearch, ¨
# Dijkstra

# Linear
def Linear():
    array = []
    keyword = 10
    for x in range(15):
        array.append(random.randint(0, 10))

    for i in range(len(array)):
        if array[i] == keyword:
            print(keyword, " found")
            # break if only searching for one
Linear()
print("End of Example \n ")

def binarySearch():
    array = []
    keyword = 10
    for x in range(15):
        array.append(random.randint(0, 10))
    
    left, right = 0, len(array) - 1
    while left <= right:
        # Mitte berechnen linker Index (Start 0) + Letzter Index dividiert durch 2
        mid = (left + right) // 2
        # Wenn die Mitte == Keyword ist dann ist der Wert gefunden
        if array[mid] == keyword:
            print(keyword)
            break # sonst endlos print loop wegen while 

        # Wenn der Wert in Mitte < ist als der gesuchte Wert wir links = mitte + 1 gesetzt
        elif array[mid] < keyword:
            left = mid + 1
        # Wenn der Wert in Mitte > ist als der gesuchte Wert wir rechts = mitte -  1 gesetzt
        else: 
            right = mid + -1

binarySearch()
print("End of Example \n ")
