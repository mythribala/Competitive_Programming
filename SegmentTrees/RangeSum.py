'''
Given Two type of queries :
Type 1 : 1 pos val --> Change value of the element at the index 'pos' to 'val'
Type 2 : 2 L R     --> Give the Sum of elements in the range L to R (both inclusive)

Example : 
arr = [1, 2, 3, 4]
2 0 3 --> 10 (1 + 2 + 3 + 4)
1 1 10 --> arr changes to [1, 10, 3, 4]
2 0 3 --> 18 (1 + 10 + 3 + 4)

'''

def BuildTree(index, start, end) :
    if (start == end) :
        sgt[index] = arr[start]
        return

    mid = (start + end) // 2
    BuildTree(2 * index, start, mid)
    BuildTree(2 * index + 1, mid + 1, end)
    sgt[index] = sgt[2 * index] + sgt[2 * index + 1]

def Update(index, start, end, tIndex, tValue) :
    if (start == end) :
        arr[start] = tValue
        sgt[index] = tValue
        return
    mid = (start + end) // 2
    if (tIndex <= mid) :
        Update(2 * index, start, mid, tIndex, tValue)
    else :
        Update(2 * index + 1, mid + 1, end, tIndex, tValue)
    sgt[index] = sgt[2 * index] + sgt[2 * index + 1]

def Query(index, start, end, qL, qR) :
    if (start >= qL and end <= qR) :
        return sgt[index]
    if (start > qR or end < qL) :
        return 0 
    mid = (start + end) // 2
    ansL = Query(2 * index, start, mid, qL, qR)
    ansR = Query(2 * index + 1, mid + 1, end, qL, qR)
    return ansL + ansR


#Example

n = 3
arr = [1, 3, 5]
sgt = [0] * (4 * n)
BuildTree(1, 0, n - 1)
print(Query(1, 0, n - 1, 0, 2))
Update(1, 0, n - 1, 1, 2)
print(Query(1, 0, n - 1, 0, 2))