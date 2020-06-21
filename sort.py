import time
from datetime import datetime
from createList import randomList

def mergeSort(myList, delay=[0]):
    ## Esta versão do Merge Sort não tem bom desempenho mas serve para demonstração
    l = 0
    r = len(myList) - 1
    doMergeSort(myList, l, r, delay=delay)

def doMergeSort(myList, l, r, delay=[0]):
    listSize = r - l + 1
    if(listSize > 2):
        m = int(listSize / 2)
        doMergeSort(myList, l, l+m-1, delay=delay)
        doMergeSort(myList, l+m, r, delay=delay)
        merge(myList, l, l+m-1, l+m, r, delay=delay)
    elif(listSize == 2):
        if(myList[l] > myList[r]):
            aux = myList[r]
            myList[r] = myList[l]
            myList[l] = aux
            time.sleep(delay[0]*4)

def merge(myList, l1, r1, l2, r2, delay=[0]):
    copyList = myList.copy()
    i = r2
    while(r1 >= l1 or r2 >= l2):
        if(r1 < l1):
            myList[i] = copyList[r2]
            time.sleep(delay[0]*4)
            r2 -= 1
            i -= 1
        elif(r2 < l2):
            myList[i] = copyList[r1]
            time.sleep(delay[0]*4)
            r1 -= 1
            i -= 1
        else:
            if(copyList[r1] > copyList[r2]):
                time.sleep(delay[0]*4)
                myList[i] = copyList[r1]
                r1 -= 1
            else:
                myList[i] = copyList[r2]
                time.sleep(delay[0]*4)
                r2 -= 1
            i -= 1

def bubbleSort(myList, delay=[0]):
    listSize = len(myList)
    for i in range(listSize - 1):
        for j in range(listSize - 1 - i):
            if(myList[j] > myList[j + 1]):
                aux = myList[j+1]
                myList[j+1] = myList[j]
                myList[j] = aux
                if(delay[0] != 0):
                    time.sleep(delay[0]*4)

def quickSort(myList, delay=[0]):
    doQuickSort(myList, 0, len(myList), delay=delay)

def doQuickSort(myList, l, r, delay=[0]):
    tempL = l
    tempR = r - 2
    listSize = r - l
    # chose a pivot
    ## Ordena o primeiro, o ultimo e o elemento do meio e usa o meio como pivot
    if(listSize > 2):
        m = l + int(listSize/2)
        if(myList[l] > myList[m]):
            aux = myList[m]
            myList[m] = myList[l]
            myList[l] = aux
            time.sleep(delay[0]*4)
        if(myList[m] > myList[r-1]):
            aux = myList[r-1]
            myList[r-1] = myList[m]
            myList[m] = aux
            time.sleep(delay[0]*4)
        if(myList[l] > myList[m]):
            aux = myList[m]
            myList[m] = myList[l]
            myList[l] = aux
            time.sleep(delay[0]*4)
        if(listSize > 3):
            pivot = myList[m]
            # Move o pivot pra direita
            aux = myList[r-1]
            myList[r-1] = myList[m]
            myList[m] = aux
            # doSort 
            while(tempL < tempR):
                while(myList[tempL] < pivot and tempL < len(myList)):
                    tempL += 1
                while(myList[tempR] >= pivot and tempR >= 0):
                    tempR -= 1
                if(tempL < tempR):
                    aux = myList[tempR]
                    myList[tempR] = myList[tempL]
                    myList[tempL] = aux
                    time.sleep(delay[0]*16)
            aux = myList[tempL]
            myList[tempL] = myList[r - 1]
            myList[r - 1] = aux
            time.sleep(delay[0]*4)
            doQuickSort(myList, l, tempL, delay=delay)
            doQuickSort(myList, tempL + 1, r, delay=delay)
    elif(listSize == 2):
        if(myList[l] > myList[r - 1]):
            aux = myList[r - 1]
            myList[r - 1] = myList[l]
            myList[l] = aux
            time.sleep(delay[0]*4)

def testAlg(alg):
    exTime = 0
    listSize = 100
    while(exTime < 60):
        myList = randomList(listSize, listSize*2)
        copyList = myList.copy()
        copyList.sort()
        startTime = datetime.now().timestamp()
        alg(myList)
        endTime = datetime.now().timestamp()
        exTime = endTime - startTime
        listSize *= 2

        print('N:  ', listSize, '   Time:  ', exTime, '  A Lista está ordenada? ', copyList == myList)

def testeSort():
    exTime = 0
    listSize = 100
    while(exTime < 30):
        myList = randomList(listSize, listSize*2)
        startTime = datetime.now().timestamp()
        myList.copy()
        endTime = datetime.now().timestamp()
        exTime = endTime - startTime
        listSize *= 2
        print('N:  ', listSize, '   Time:  ', exTime,)

if __name__ == "__main__":
    testeSort()