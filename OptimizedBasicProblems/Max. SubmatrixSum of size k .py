'''
Problem : Given a matrix of Size N * N and an integer K, print the maximum sum of the submatrix of size K * K

Approach : Using C^2 column sum approach + PrefSum

T.C : O(C * (3 * R)) ~ O(C * R)

Problem Link : https://www.geeksforgeeks.org/problems/coins-of-geekland--141631/1 

'''

#Code 

class Solution:
    def Maximum_Sum(self, mat, N, K):
        
        rowSum = [0] * N
        for col in range(K - 1) :
            for row in range(N) :
                rowSum[row] += mat[row][col]
        
        left = 0
        right = K - 1
        res = -float('inf')
        for right in range(K - 1, N):
            
            for row in range(N) :
                rowSum[row] += mat[row][right]
            
            innerLeft = curSum = 0
            for innerRight in range(N) :
                curSum += rowSum[innerRight]
                if (innerRight - innerLeft == K) :
                    curSum -= rowSum[innerLeft]
                    innerLeft += 1
                if (innerRight - innerLeft + 1 == k) :
                    res = max(res, curSum)
            
            for row in range(N) :
                rowSum[row] -= mat[row][left]
            
            left += 1
        
        return res