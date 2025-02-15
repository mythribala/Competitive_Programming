'''
Given Two type of queries :
Type 1 : 1 pos val --> Change value of the element at the index 'pos' to 'val'
Type 2 : 2 L R     --> Give the Second Minimum elements in the range L to R (both inclusive)

Example : 
arr = [100, 25, 13, 40]
2 0 3 --> 25
1 1 10 --> arr changes to [100, 10, 13, 40]
2 0 3 --> 13


BuildTree : Store -> [FirstMin, SecondMin]   (In leaf node, store as : [arr[start], float('inf)])
            Combine -> Add left and right child and then sort them and keep the first and second Minimum only

Update : Similar to simple RangeSum update

Query : Full overlap : return sgt[index]
        No overlap : return [-float('inf), -float('inf')]
        Partial overlap : Call left and right child and perform Combine operation similar to BuildTree Combine

'''

def  ComputeInternalNode(index) :
    left = sgt[2 * index]
    right = sgt[2 * index + 1]
    combined = sorted(left + right)[ : 2]
    return combined

def BuildTree(index, start, end) :
    if (start == end) :
        sgt[index] = [arr[start], float('inf')]
        return
    else :
        mid = (start + end) // 2
        BuildTree(2 * index, start, mid)
        BuildTree(2 * index + 1, mid + 1, end)
        sgt[index] = ComputeInternalNode(index)

def Update(index, start, end, tIndex, tValue) :
    if (start == end) :
        arr[start] = tValue
        sgt[index][0] = tValue
        return
    else :
        mid = (start + end) // 2
        if (tIndex <= mid) :
            Update(2 * index, start, mid, tIndex, tValue)
        else :
            Update(2 * index + 1, mid + 1, end, tIndex, tValue)
        sgt[index] = ComputeInternalNode(index)

def Query(index, start, end, qL, qR) :
    if (start >= qL and end <= qR) :
        return sgt[index]
    
    if (start > qR or end < qL) :
        return [float('inf'), float('inf')]

    mid = (start + end) // 2
    ansL = Query(2 * index, start, mid, qL, qR)
    ansR = Query(2 * index + 1, mid + 1, end, qL, qR)
    combined = sorted(ansL + ansR)[ : 2]
    return combined