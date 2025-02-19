'''

Template of Generic Segment Tree in Python

'''



#Modification for 1st Segment Tree (E.g : Range minimum)

class Node1:
    def __init__(self, index = -1, val = float('inf')):  # Default element -> Will change
        self.val = val                  # May change
    
    def merge(self, left, right):  # Merge two child nodes
        self.val = min(left.val, right.val)  # May change

class Update1:
    def __init__(self, val):  
        self.val = val
    
    def apply(self, node):  # Apply update to given node
        node.val = self.val  # May change

#Modification for 2nd Segment Tree (E.g : Range maximum)

class Node2 :
    def __init__(self, index = -1, val = -float('inf')):
        self.val = val

    def merge(self, left, right):
        self.val = max(left.val, right.val)

class Update2:
    def __init__(self, val):
        self.val = val

    def apply(self, node):
        node.val = self.val

''' Generic Segment Tree Template '''

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

#----------------------------------------------------------------------#
# Example -> Find Both minimum and maximum in a given range (l, r) with point updates

n = int(input())
arr = list(map(int, input().split()))
queries = int(input())

sgt1 = SegmentTree(n, arr, Node1, Update1)
sgt2 = SegmentTree(n, arr, Node2, Update2)

for _ in range(queries):
    typ = int(input())
    if typ == 1:
        pos, val = map(int, input().split())
        sgt1.make_update(pos, val)
        sgt2.make_update(pos, val)
    else:
        l, r = map(int, input().split())
        ans1 = sgt1.make_query(l, r)
        ans2 = sgt2.make_query(l, r)
        print(ans1.val, ans2.val)

#----------------------------------------------------------------------------------------------#