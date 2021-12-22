import random
import time

def quickSort (unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    referenceElem = unsortedList.pop(int(len(unsortedList)/2))
    lessThanRef = []
    moreThanRef = []
    for i in unsortedList:
        if i < referenceElem:
            lessThanRef.append(i)
        else:
            moreThanRef.append(i)   
    return (quickSort(lessThanRef) + [referenceElem] + quickSort(moreThanRef)) 
    

def bubbleSort(unsortedList):
    for i in range(len(unsortedList)-1):
        for j in range(len(unsortedList)-i-1):
            if unsortedList[j] > unsortedList[j+1]:
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
    return unsortedList


def stupidSort(unsortedList):
    for i in range(len(unsortedList)-1):
        for j in range(len(unsortedList)-1):
            for k in range(len(unsortedList)-1):
                if unsortedList[k] > unsortedList[k+1]:
                    unsortedList[k], unsortedList[k+1] = unsortedList[k+1], unsortedList[k]
                    break
    return unsortedList

def shakerSort(unsortedList):
    noSwap = False
    while not noSwap:
        noSwap = True
        for j in range(len(unsortedList)-1):
            if unsortedList[j] > unsortedList[j+1]:
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
                noSwap = False
        for j in range(len(unsortedList)-1, 1, -1):
            if unsortedList[j-1] > unsortedList[j]:
                unsortedList[j], unsortedList[j-1] = unsortedList[j-1], unsortedList[j]
                noSwap = False
    return unsortedList

if __name__ == "__main__":
    listLen = 300
    maxRandom = 100
    minRandom = 1
    
    dummyList = [random.randint(minRandom, maxRandom) for i in range(listLen)]

    dummyListCopy1 = dummyList.copy()
    dummyListCopy2 = dummyList.copy()
    dummyListCopy3 = dummyList.copy()
    dummyListCopy4 = dummyList.copy()
        
    bubbleTime = time.time()
    dummyListCopy1 = bubbleSort(dummyListCopy1)
    bubbleTime = time.time() - bubbleTime
    print("bubble sorting time ", bubbleTime)

    quickTime  = time.time()
    dummyListCopy2 = quickSort(dummyListCopy2)
    quickTime = time.time() - quickTime
    print("quick  sorting time ", quickTime)

    stupidTime = time.time()
    dummyListCopy3 = stupidSort(dummyListCopy3)
    stupidTime = time.time() - stupidTime
    print("stupid sorting time ", stupidTime)    

    shakerTime = time.time()
    dummyListCopy4 = shakerSort(dummyListCopy4)
    shakerTime = time.time() - shakerTime
    print("shaker sorting time ", shakerTime)   

    print()
    if not (dummyListCopy1 == dummyListCopy2 == dummyListCopy3 == dummyListCopy4):
        print("lists don't match") 
    
