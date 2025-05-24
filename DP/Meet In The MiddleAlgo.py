'''

LC 1755. Closest Subsequence Sum
Algorithm used : Meet In The Middle (MIM)
     Intuition : Step 1 : Split the total array 'nums' into two nearly equal arrays 'arr1' and 'arr2'
                 Step 2 : Find all possible subset sums of both the arrays separately, say 'set1' and 'set2'
                 Step 3 : Sort the second subset 'set2'
                 Step 4 : Iterate through each subset sum in 'set1' and using binary search find the element which is near to 'target - num' from 'set2'

T.C : naive Solution : O(2 ^ N)
      MIM Algorithm  : Step 1 : O(1)
                       Step 2 : O(2 ^ (N/2) + 2 ^ (N/2))
                       Step 3 : O(2 ^ (N/2) * log(2 ^ (N/2)))  ~ O((N/2) * 2 ^ (N/2))
                       Step 4 : O(2 ^ (N/2) * log(2 ^ (N/2)))  ~ O((N/2) * 2 ^ (N/2))
                       Total T.C => approx. <= 10**8
                 
'''

#Code

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def generateSubsets(arr) :

            def helper(ind, curSum) :
                if (ind == m) :
                    res.append(curSum)
                    return
                helper(ind + 1, curSum + arr[ind])
                helper(ind + 1, curSum)

            m = len(arr)
            res = []
            helper(0, 0)
            return res

        n = len(nums)
        mid =  n // 2
        set1 = generateSubsets(nums[ : mid])
        set2 = generateSubsets(nums[mid : ])
        set2.sort()
        m = len(set2)
        res = float('inf')
        for num in set1 :
            idx2 = bisect_left(set2, goal - num)
            if (idx2 < m) :
                res = min(res, abs(goal - (num + set2[idx2])))
            if (idx2 - 1 >= 0) :
                idx2 -= 1
                res = min(res, abs(goal - (num + set2[idx2])))
        
        return res  
