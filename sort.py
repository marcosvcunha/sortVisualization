import time

def mergeSort(myList, delay=[0]):
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

def merge_sort(myList):
    sortedList = do_merge_sort(myList.copy())
    for i in range(len(myList)):
        myList[i] = sortedList[i]

def do_merge_sort(unsorted_list):
    listSize = len(unsorted_list)
    if(listSize > 1):
        middle = int(listSize/2)
        leftHalf = do_merge_sort(unsorted_list[:middle])
        rightHalf = do_merge_sort(unsorted_list[middle:])
        return merge2(leftHalf, rightHalf)
    else:
        return unsorted_list
# Merge the sorted halves

def merge2(left_half,right_half):
    sortedList = []
    i = 0
    j = 0
    while (i < len(left_half) and j < len(right_half)):
        if(left_half[i] < right_half[j]):
            sortedList.append(left_half[i])
            i += 1
        else:
            sortedList.append(right_half[j])
            j += 1
    
    if(i < len(left_half)):
        sortedList += left_half[i:]
    else:
        sortedList += right_half[j:]
    return sortedList
        

