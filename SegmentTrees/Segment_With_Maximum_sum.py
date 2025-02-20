'''

Problem Name : Segment with the Maximum Sum

In this problem, we need to write a segment tree to find the segment with the maximum sum.
Problem Link : https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A

'''

class Node1:
    def __init__(self, index = -1, val = 0):  
        self.pref = val
        self.suff = val
        self.sum = val
        self.maximum = val

    def merge(self, left, right):  
        self.maximum = max(left.maximum, right.maximum, left.suff + right.pref)
        self.pref = max(left.pref, left.sum  + right.pref)
        self.suff = max(right.suff, right.sum + left.suff)
        self.sum = left.sum + right.sum

class Update1:
    def __init__(self, val):  
        self.val = val

    def apply(self, node): 
        node.pref = self.val
        node.suff = self.val
        node.sum = self.val
        node.maximum = self.val

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

ans = sgt.make_query(0, n - 1)
print(max(0, ans.maximum))

for _ in range(queries):
    pos, val = tuple(map(int, input().split()))
    sgt.make_update(pos, val)
    ans = sgt.make_query(0, n - 1)
    print(max(0, ans.maximum))