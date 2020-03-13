from random import randint
import time

tab = [randint(1, 100) for i in range(50)]
print(*tab)

start_time=time.time()
def selectionSort(tab):
    tablica = [tab[i] for i in range(len(tab))]
    for i in range (len(tablica)-1):
        min_element=i
        for pozycja in range (i, len(tablica)):
            if tablica[pozycja]<tablica[min_element]:
                min_element=pozycja
        tablica[min_element], tablica[i]=tablica[i], tablica[min_element]
    return tablica

print("\nSelection Sort\n---- %7e sek ----" % (time.time()-start_time))
print(selectionSort(tab))
start_time=time.time()

def insertionSort(tab):
    tablica = [tab[i] for i in range(len(tab))]
    for i in range (1, len(tablica)):
        curr = tablica[i]
        pozycja = i

        while (pozycja > 0) and (tablica[pozycja-1] > curr):
            tablica[pozycja] = tablica[pozycja-1]
            pozycja -= 1

        tablica[pozycja] = curr
    return tablica

print("\nInsertion Sort\n---- %7e sek ----" %(time.time()-start_time))
print(insertionSort(tab))
start_time=time.time()

def bubbleSort(tab):
    tablica = [tab[i] for i in range(len(tab))]
    for i in range(len(tablica)-1):
        for j in range(len(tablica)-1):
                if tablica[j] > tablica[j+1]:
                    tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    return tablica

print("\nBubble Sort\n---- %7e sek ----" %(time.time()-start_time))
print(bubbleSort(tab))
start_time=time.time()

def quickSort(tab):
    tablica = [tab[i] for i in range(len(tab))]

    if len(tablica) <= 1:
        return tablica

    pivot = tablica[0]

    mniejsze = []
    for i in tablica:
        if i < pivot:
            mniejsze.append(i)

    rowne = []
    for i in tablica:
        if i == pivot:
            rowne.append(i)

    wieksze = []
    for i in tablica:
        if i > pivot:
            wieksze.append(i)

    return quickSort(mniejsze) + rowne + quickSort(wieksze)

print("\nQuick Sort\n---- %7e sek ----" %(time.time()-start_time))
print(quickSort(tab))
start_time=time.time()

def mSort(tab):
    tablica = [tab[i] for i in range(len(tab))]
    mergeSort(tablica)
    return tablica


def mergeSort(tablica):
    if len(tablica) > 1:
        sr = len(tablica) // 2
        lewo = tablica[:sr]
        prawo = tablica[sr:]

        mergeSort(lewo)
        mergeSort(prawo)

        i = j = n = 0
        while i < len(lewo) and j < len(prawo):
            if lewo[i] < prawo[j]:
                tablica[n] = lewo[i]
                i += 1
            else:
                tablica[n] = prawo[j]
                j += 1
            n += 1

        while i < len(lewo):
            tablica[n] = lewo[i]
            i += 1
            n += 1

        while j < len(prawo):
            tablica[n] = prawo[j]
            j += 1
            n += 1
    return tablica

print("\nMerge Sort\n---- %7e sek ----" %(time.time()-start_time))
print(mSort(tab))
start_time=time.time()

def bucketSort(tab):
    tablica=[tab[i] for i in range(len(tab))]
    tablica1=[]
    buckets = [[] for i in range(101)]
    for i in tablica:
        for a in range(len(buckets)):
            if i==a:
                buckets[a].append(i)
    for a in range(len(buckets)):
        for i in range(len(buckets[a])):
            if buckets[a][i]!='':
                tablica1.append(buckets[a][i])
    return tablica1

print("\nBucket Sort\n---- %7e sek ----" %(time.time()-start_time))
print(bucketSort(tab))
start_time=time.time()

def kopiec(tab, n, i):
    najwiekszy = i
    l = 2 * i + 1
    p = 2 * i + 2

    if l < n and tab[i] < tab[l]:
        najwiekszy = l

    if p < n and tab[najwiekszy] < tab[p]:
        najwiekszy = p

    if najwiekszy != i:
        tab[i], tab[najwiekszy] = tab[najwiekszy], tab[i]
        kopiec(tab, n, najwiekszy)

def heap_sort(tab):
    n = len(tab)
    i=n
    while i > 0:
        kopiec(tab, n, i)
        i-=1
    i=n-1
    while i > 0:
        tab[i], tab[0] = tab[0], tab[i]
        i-=1
        kopiec(tab, i, 0)

def heapSort(tab):
    tablica=[tab[i] for i in range(len(tab))]
    heap_sort(tablica)
    return tablica

print("\nHeap Sort\n---- %7e sek ----" %(time.time()-start_time))
print(heapSort(tab))
start_time=time.time()

def radixSort(tab):
    tablica = [tab[i] for i in range(len(tab))]
    a = max(tablica)
    q = 0
    while a != 0:
        a //= 10
        q += 1
    s = 0
    while s < q:
        lista = [[] for i in range(10)]
        for i in tablica:
            r = int(i // (10 ** s) % 10)
            lista[r].append(i)

        k = 0
        for i in range(10):
            for j in lista[i]:
                tablica[k] = j
                k += 1

        s += 1
    return tablica

print("\nRadix Sort\n---- %7e sek ----" %(time.time()-start_time))
print(radixSort(tab))
start_time=time.time()


