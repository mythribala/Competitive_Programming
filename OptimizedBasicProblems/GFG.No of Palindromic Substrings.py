'''
Problem Link : https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

Examples :

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings are : "aba" , "aa" , "baab".

Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings are : "aa", "aa", "aaa".

Solution :

Brute Force : Generating all possible substrings and checking for Palindrome property : T.C -> O(n^3)
Optimal Approach : Using Central Expansion Method : T.C -> O(n^2)

'''

#Code

class Solution:

    def countPS(self, s):
        
        def isOddPalindrome(x) :
            cur = 0
            i = x - 1
            j = x + 1
            while (i >= 0 and j < n and s[i] == s[j]) :
                cur += 1
                i -= 1
                j += 1
            return cur
        
        
        def isEvenPalindrome(x) :
            cur = 0
            i = x - 1
            j = x
            while (i >= 0 and j < n and s[i] == s[j]) :
                cur += 1
                i -= 1
                j += 1
            return cur
        
        res = 0
        n = len(s)
        for i in range(n) :
            res += isOddPalindrome(i)
            if (i > 0) :
                res += isEvenPalindrome(i)
        
        return res
