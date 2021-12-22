import random

def qSort (unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    referenceElem = unsortedList.pop(int(len(unsortedList)/2))
    lessThanRef = []
    moreThanRef = []
    # print(referenceElem)
    for i in unsortedList:
        if i < referenceElem:
            lessThanRef.append(i)
        else:
            moreThanRef.append(i)   
    return (qSort(lessThanRef) + [referenceElem] + qSort(moreThanRef))

if __name__ == "__main__":
    listLen = 100
    dummyList = [random.randint(1, 100) for i in range(listLen)]
    print(dummyList)
    print()
    dummyList = qSort(dummyList)
    print()
    print(dummyList)
