# 26. Implementiere die Ubungen des Python-Codelabs: BubbleSort
# BucketSort, CountingSort, InsertionSort, Quicksort, SelectionSort, BrickSort
import time
import random


listOfNumbersBubble = []
for i in range(1000):
    listOfNumbersBubble.append(random.randint(0, 1000))

listOfFloatsBucket = []
for i in range(1000):
    listOfFloatsBucket.append(random.random())

listOfNumbersInsertion = []
for i in range(1000):
    listOfNumbersInsertion.append(random.randint(0, 1000))

arr = []
for i in range(1000):
    arr.append(random.randint(0, 1000))

array = []
for i in range(100):
    array.append(random.randint(0, 1000))



#BUBBLE
def BubbleSort(listOfNumbers):
    startTime = time.time()
    n = len(listOfNumbers)
    for i in range(n):
        for j in range(0, n-1-i):
            if listOfNumbers[j] > listOfNumbers[j+1]:
                listOfNumbers[j], listOfNumbers[j+1] = listOfNumbers[j+1], listOfNumbers[j]
    endTime = time.time()
    print("Sorting with Bubble Sort took ", endTime - startTime)
    print("\n")




#BUCKET
def BucketInsertion(bucket):
    for i in range(len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[i]
            j -= 1
        bucket[j + 1] = key

def BucketSort(listOfNumbers):
    startTime = time.time()
    n = len(listOfNumbers)
    buckets = [[] for _ in range(n)]

    for number in listOfNumbers:
        bi = int(n * number)
        buckets[bi].append(number)

    for bucket in buckets:
        BucketInsertion(bucket)

    index = 0
    for bucket in buckets:
        for number in bucket:
            listOfNumbers[index] = number
            index += 1
    endTime = time.time()
    print("Sorting with Bucket Sort took ", endTime - startTime)
    print("\n")




def InsertionSort(listOfNumbersInsertion):
    startTime = time.time()
    for i in range(len(listOfNumbersInsertion)):
        key = listOfNumbersInsertion[i]
        j = i - 1
        while j >= 0 and listOfNumbersInsertion[j] > key:
            listOfNumbersInsertion[j + 1] = listOfNumbersInsertion[i]
            j -= 1
        listOfNumbersInsertion[j + 1] = key
    endTime = time.time()
    print("Sorting with Insertion Sort took ", endTime - startTime)
    print("\n")


def BrickSort(arr):
    startTime = time.time()
    n = len(arr)
    isSorted = 0
    while isSorted == 0: 
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
                 
        for i in range(0, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
    endTime = time.time()
    print("Brick sort took ", endTime - startTime)

# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array


BubbleSort(listOfNumbersBubble)
BucketSort(listOfFloatsBucket)
InsertionSort(listOfNumbersInsertion)
BrickSort(arr)
countingSort(array)
input()

# 27. Was ist der 
# schnellste, was ist der langsamste Sortieralgorithmus? Welche Speicher- und Zeitkomplexit¨aten weißen
# diese auf?

# Der schellste ist der QuickSort durch die vielen aufteillungen, wodurch man ihn auch parallelisysieren kann
# Der langsamste ist der Bubble Sort da er 2 mal die Ganze Liste durchgehen muss
