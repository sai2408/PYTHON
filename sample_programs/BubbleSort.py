

def bubbleSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ) :
        for j in range( n-i-1) :
            if theSeq[j] > theSeq[j + 1] :
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp


arr=[5,4,3,2,1]
bubbleSort(arr)
print(arr)





