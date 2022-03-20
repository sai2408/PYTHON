
def insertionSort( theSeq ):
    n = len( theSeq )
    for i in range( 1, n ) :
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1] :
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value


arr=[5,1,8,3,9,2]
insertionSort(arr)
print(arr)
