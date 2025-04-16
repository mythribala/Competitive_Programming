'''

Problem Link : https://leetcode.com/problems/count-good-triplets-in-an-array

'''

'''
Solution : Using SegmenTree + Hashing
           Query -> query each time at index 'i' to get the no. of common elements between 0 - index of nums1[i] at nums2
           Build -> Build each time such that which sets index of nums1[i] at nums2 = 1 and updates the range sum using merge

T.C      : O(N*log(n))           
'''

#CODE 

class Node1:
    def __init__(self, index = -1, val = 0):  
        self.val = val                 
    
    def merge(self, left, right):  
        self.val = left.val + right.val

class Update1:
    def __init__(self, val):  
        self.val = val
    
    def apply(self, node): 
        node.val = self.val

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

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        idx_map = {ele : ind for ind, ele in enumerate(nums2)}
        res = 0
        sgt = SegmentTree(n, nums1, Node1, Update1)
        for i in range(n) :
            ind = idx_map[nums1[i]]
            common_left = sgt.make_query(0, ind).val
            uncommon_left = (i - common_left)
            common_right = (n - (ind + 1) - uncommon_left)
            res += (common_left * common_right)
            sgt.make_update(ind, 1)
        return res