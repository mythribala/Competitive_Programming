'''

Problem name : Aggressive Cows
Topic : Binary Search on Answers

'''

#Code

class Solution:

    def aggressiveCows(self, stalls, k):
        
        def check(m) :
            curStalls = 1
            prevStall = stalls[0]
            for i in range(1, n) :
                if (stalls[i] - prevStall >= m) :
                    curStalls += 1
                    prevStall = stalls[i]
                if (curStalls == k) :
                    return True
            return False


        stalls.sort()
        n = len(stalls)
        res = 0
        low = 0
        high = stalls[n - 1] - stalls[0]
        while (low <= high) :
            mid = ((low - high) // 2) + high
            if (check(mid)) :
                res = mid
                low = mid + 1
            else :
                high = mid - 1
        return res