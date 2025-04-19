'''
Problem link : https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1

Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. Find the two numbers in decreasing order which has odd occurrences.

Example 1:

Input:
N = 8
Arr = {4, 2, 4, 5, 2, 3, 3, 1}
Output: {5, 1} 
Explanation: 5 and 1 have odd occurrences.

Solution : Approach 1 : Using HashMap -> T.C : O(n), S.C : O(n)
           Approach 2 : Using Count based Sorting -> T.C : O(nlog(n)), S.C : O(1)
           Optimized Approach : Using Bit Manipulation -> T.C : O(n), S.C : O(1)

Intuition : We first take up the totalXor value of all the elements which gives us the xor of 'Two odd occuring elements'. 
            Now based on any position of the setBit on the totalXor (Here I prefered the leftmost first position), we separate 
            the elements in the list into two groups (1. with the particular position set AND 2. with the particular position unset)
            Now the separate xors for both the groups gives us the required two elements.
'''

#Code 

class Solution:
    def twoOddNum(self, Arr, N):
        totalXor = 0
        for each in Arr :
            totalXor ^= each
        for i in range(30) :
            if (totalXor & (1 << i)) :
                cur = (1 << i)
                break
        num1 = 0
        num2 = 0
        for each in Arr :
            if (each & cur) :
                num1 ^= each
            else :
                num2 ^= each
        
        return sorted([num1, num2], reverse = True)