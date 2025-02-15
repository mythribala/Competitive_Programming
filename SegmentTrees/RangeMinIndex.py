'''
Given Two type of queries :
Type 1 : 1 pos val --> Change value of the element at the index 'pos' to 'val'
Type 2 : 2 L R     --> Give the First Index of Minimum element in the range L to R (both inclusive)

Example : 
arr = [100, 25, 13, 40, 13]
2 0 4 --> 2 (arr[2] is the first minimum element)
1 1 5 --> arr changes to [100, 5, 13, 40, 13]
1 4 1 --> arr changes to [100, 5, 13, 40, 1]
2 0 3 --> 1 (arr[1] = 5, which is the smallest in [100, 5, 13, 40])

BuildTree : Store -> Index of the Minimum element (In leaf node, store as : sgt[index] = start)
            Combine -> if (arr[LeftChild] <= arr[RightChild]) : sgt[index] = LeftChild, else : sgt[index] = RightChild

Update : Similar to simple Range Minimum update

Query : Full overlap : return sgt[index]
        No overlap : return -1 and should handle it
        Partial overlap : Call left and right child and perform Combine operation similar to BuildTree Combine with checking whether it is not -1

'''

def Combine(index) :
    left = arr[sgt[2 * index]]
    right = arr[sgt[2 * index + 1]]
    if (left <= right) :
        return sgt[2 * index]
    else :
        return sgt[2 * index + 1]

def BuildTree(index, start, end) :
    if (start == end) :
        sgt[index] = start
    else :
        mid = (start + end) // 2
        BuildTree(2 * index, start, mid)
        BuildTree(2 * index + 1, mid + 1, end)
        sgt[index] = Combine(index)

def Update(index, start, end, tIndex, tValue) :
    if (start == end) :
        arr[start] = tValue
    else :
        mid = (start + end) // 2
        if (tIndex <= mid) : 
            Update(2 * index, start, mid, tIndex, tValue)
        else :
            Update(2 * index + 1, mid + 1, end, tIndex, tValue)
        sgt[index] = Combine(index)

def Query(index, start, end, qL, qR) :
    if (start >= qL and end <= qR) :
        return sgt[index]
    elif (start > qR or end < qL) :
        return -1
    else :
        mid = (start + end) // 2
        ansL = Query(2 * index, start, mid, qL, qR)
        ansR = Query(2 * index + 1, mid + 1, end, qL, qR)
        if (ansL == -1) :
            return ansR
        elif (ansR == -1) :
            return ansL
        elif (arr[ansL] <= arr[ansR]) :
            return ansL
        else :
            return ansR

#Example

n = int(input())
sgt = [0] * (4 * n)
arr = list(map(int,input().split()))
q = int(input())
BuildTree(1, 0, n - 1)
for _ in range(q) :
    x, l, r = tuple(map(int,input().split()))
    if (x == 1) :
        Update(1, 0, n - 1, l, r)
    else :
        ans = Query(1, 0, n - 1, l, r)
        print(ans)