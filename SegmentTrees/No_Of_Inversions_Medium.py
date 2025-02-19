'''

Problem Name : Number of Inversions on Segment
Problem Link : https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C  
Submission Link : https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/306866276

Jist : Given Two types of queries 
       1 -> pos, val -> Update the value of element at index 'pos' to value 'val'
       2 -> left, right -> Find the number of Inversions in the given range 'left' to 'right' (both inclusive)
       Note : 1 <= a[i] <= 40 

Approach : At each node : Store the 'current no. of inversions' and also the 'frequency of all elements in the segment'
           i.e, At leaf node : 'current no. of inversions' = 0 (as one element can't have any inversion) and 'freq array' = 0 for all elements except the current index element
                At internal node : 'current no. of inversions' = leftChild.inversions + rightChild.inversions + for all elements in the left child -> left.freq[i] * no of elements less than i in the right child

'''

class Node1:
    def __init__(self, index = -1, val = 0):  
        self.val = val
        self.inversions = 0
        self.freq = [0] * (41)
        self.freq[val] += 1                  
    
    def merge(self, left, right):  
        self.inversions = left.inversions + right.inversions  
        pref_sum = 0  
        for i in range(1, 41) :
            self.inversions += (left.freq[i] * pref_sum)
            pref_sum += right.freq[i]
            self.freq[i] = left.freq[i] + right.freq[i]

class Update1:
    def __init__(self, val):  
        self.val = val
    
    def apply(self, node):
        node.freq[node.val] -= 1
        node.val = self.val
        node.freq[node.val] += 1

class SegmentTree:
    def __init__(self, n, arr, node, update):
        self.n = n
        self.arr = arr
        self.Node = node
        self.Update = update 
        self.s = 1
        while (self.s < 2 * self.n) :
            self.s <<= 1
        self.tree = [self.Node() for _ in range(self.s)]
        self.build(1, 0, self.n - 1)
    
    def build(self, index, start, end):
        if start == end:
            self.tree[index] = self.Node(start, self.arr[start])
            return
        mid = (start + end) // 2
        self.build(2 * index, start, mid)
        self.build(2 * index + 1, mid + 1, end)
        self.tree[index].merge(self.tree[2 * index], self.tree[2 * index + 1])
    
    def update_helper(self, index, start, end, query_index, update):
        if start == end:
            update.apply(self.tree[index]) 
            return
        mid = (start + end) // 2
        if query_index <= mid:
            self.update_helper(2 * index, start, mid, query_index, update)
        else:
            self.update_helper(2 * index + 1, mid + 1, end, query_index, update)
        self.tree[index].merge(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, index, start, end, left, right):
        if start > right or end < left:
            return self.Node()
        if left <= start and end <= right:
            return self.tree[index]
        mid = (start + end) // 2
        left_result = self.query(2 * index, start, mid, left, right)
        right_result = self.query(2 * index + 1, mid + 1, end, left, right)
        result = self.Node()
        result.merge(left_result, right_result)
        return result
    
    def make_update(self, index, val):
        update = self.Update(val)  
        self.update_helper(1, 0, self.n - 1, index, update)
    
    def make_query(self, left, right):
        return self.query(1, 0, self.n - 1, left, right)

n, queries = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

sgt = SegmentTree(n, arr, Node1, Update1)

for q in range(queries):
    typ, l, r = tuple(map(int, input().split()))
    l -= 1  
    if typ == 1:
        r -= 1
        ans = sgt.make_query(l, r)
        print(ans.inversions)

    else:
        pos, val = l, r
        sgt.make_update(pos, val)