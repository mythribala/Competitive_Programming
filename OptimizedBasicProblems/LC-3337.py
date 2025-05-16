'''

LeetCode 3337 : Total Characters in String After Transformations II
Topic : Matrix Exponentiation using Transformation matrix 

'''

#Code

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        
        def matMul(A, B) :  # Function to Multiply of Two matrices
            p = len(A)
            q = len(A[0])
            r = len(B[0])
            tempResMat = [[0] * (r) for j in range(p)]
            for i in range(p) :
                for j in range(r) :
                    for k in range(q) :
                        tempResMat[i][j] += (A[i][k] * B[k][j]) % MOD
            return tempResMat

        def matExpo(transMat, resMat, N) : # Matrix Exponentiation
            while(N > 0) :
                if (N % 2) :
                    resMat = matMul(resMat, transMat)
                transMat = matMul(transMat, transMat)
                N //= 2
            return resMat

        transMat = [[0] * (26) for i in range(26)] # Transformation matrix created for size 26 * 26 because of the degree being 26 (i.e, no. of terms the function depends upon)
        for i in range(26) :
            for j in range(nums[i]) :
                transMat[i][(i + j + 1) % 26] = 1
        
        resMat = [[0] * 26]
        for alpha in s :
            resMat[0][ord(alpha) - 97] += 1
        
        MOD = pow(10, 9) + 7
        cur = matExpo(transMat, resMat, t)
        return sum(cur[0]) % MOD
