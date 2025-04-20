'''
Problem Link : https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1

Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

Examples:

Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
Output: true
Explanation: 14 is present in the matrix, so output is true.

Solution :

Brute Force : Traversing through the whole matrix : T.C -> O(n*m)
Optimal Approach : Using Binary Search : T.C -> O(log(n * m)) == O(log(n)) + O(log(m))

Intuition : Imagine the 2D array as an single 1D array and mark their indices w.r.t either the row-wise or col-wise 
and perform the Binary Search with low = 0 and high = n * m - 1

'''

'''
Trick :
when a matrix is marked with col-wise : row = ind // m , col = ind % m
when a matric is marked with row-wise : row = ind % n , col = ind // n
'''

#Code

class Solution:
    
  def searchMatrix(self, mat, target):
      
      n = len(mat)
      m = len(mat[0])
      low = 0
      high = (n * m - 1)
      
      while (low <= high) :
          mid = ((low - high) // 2) + high
          curRow = mid // m
          curCol = mid % m
          if (mat[curRow][curCol] == target) :
              return True
          elif (mat[curRow][curCol] > target) :
              high = mid - 1
          else :
              low = mid + 1
      
      return False
