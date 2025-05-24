'''

LC 2035. Partition Array Into Two Arrays to Minimize Sum Difference
Algorithm Used : Modification of the MIM Algorithm

'''

#Code 

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        def generateSubset(arr) :

            def helper(ind, cnt, curSum) :
                if (ind == n) :
                    res[cnt].append(curSum)
                    return
                helper(ind + 1, cnt + 1, curSum + arr[ind])
                helper(ind + 1, cnt, curSum)

            n = len(arr)
            res = [[] for i in range(n + 1)]
            helper(0, 0, 0)
            return res
        
        n = len(nums) // 2
        set1 = generateSubset(nums[ : n])
        set2 = generateSubset(nums[n : ])
        for each in set2 :
            each.sort()
        
        res = float('inf')
        totalSum = sum(nums)
        reqSum = totalSum // 2  
        for i in range(n + 1) :
            for curSum in set1[i] :
                idx2 = bisect_left(set2[n - i], reqSum - curSum)
                if (idx2 < len(set2[n - i])) :
                    temp = curSum + set2[n - i][idx2]
                    res = min(res, abs(temp - (totalSum - temp)))
                idx2 -= 1
                if (idx2 >= 0) :
                    temp = curSum + set2[n - i][idx2]
                    res = min(res, abs(temp - (totalSum - temp)))
        return res
