'''

Problem : Give the First element Greater than X within the given Range. 
Topics invloved : **** SegmentTree + BinarySearch ****

Given Two type of queries :
Type 1 : 1 pos val --> Change value of the element at the index 'pos' to 'val'
Type 2 : 2 L R X    --> Give the First Element Greater than X in the range L to R (both inclusive)

Example : 
arr = [100, 15, 13, 40, 130]
2 0 4 10 --> 100 (100 is greater than 10 and it appears before 15)
2 0 4 100 --> 130
1 1 5 --> arr changes to [100, 5, 13, 40, 130]
2 1 3 6 --> 13

How To Solve : Think of Constructing the SegmentTree just as doing for *Finding Maximum Element in a given range* and 
               use Binary Search for Finding the First element greater than X

'''

def BuildTree(index, start, end) :
    if (start == end) :
        sgt[index] = arr[start]
    else :
        mid = (start + end) // 2
        BuildTree(2 * index, start, mid)
        BuildTree(2 * index + 1, mid + 1, end)
        sgt[index] = max(sgt[2 * index], sgt[2 * index + 1])

def Update(index, start, end, tIndex, tValue) :
    if (start == end) :
        arr[start] = tValue
        sgt[index] = tValue
    else :
        mid = (start + end) // 2
        if (tIndex <= mid) : 
            Update(2 * index, start, mid, tIndex, tValue)
        else :
            Update(2 * index + 1, mid + 1, end, tIndex, tValue)
        sgt[index] = max(sgt[2 * index], sgt[2 * index + 1])

def Query(index, start, end, qL, qR) :
    if (start >= qL and end <= qR) :
        return sgt[index]
    elif (start > qR or end < qL) :
        return -float('inf')
    else :
        mid = (start + end) // 2
        ansL = Query(2 * index, start, mid, qL, qR)
        ansR = Query(2 * index + 1, mid + 1, end, qL, qR)
        return max(ansL, ansR)


n = int(input())
sgt = [0] * (4 * n)
arr = list(map(int,input().split()))
q = int(input())
BuildTree(1, 0, n - 1)
for _ in range(q) :
    qType = int(input())
    if (qType == 1) :
        pos, val = tuple(map(int,input().split()))
        Update(1, 0, n - 1, pos, val)
    else :
        l, r, x = tuple(map(int,input().split()))
        low = l  
        high = r  
        res = float('inf')
        while (low <= high) :
            mid = (low + high) // 2  
            if ( Query(1, 0, n - 1, low, mid) > x ) :
                res = arr[mid]
                high = mid - 1
            else :
                low = mid + 1
        if (res == float('inf')) :
            print('No element in the given range is Greater than :', x)
        else :
            print(res)
