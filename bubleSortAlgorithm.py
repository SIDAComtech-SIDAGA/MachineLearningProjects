arr = [7,2,3,4,2,6,9,8,44,6,7,2,1,0,1]

def bubblesort(theseq):
    n = len(theseq)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if theseq[j] > theseq[j+i]:
                temp = theseq[j]
                theseq[j] = theseq[j+1]
                theseq[j+1] = temp
    return theseq

print(bubblesort(arr))
    