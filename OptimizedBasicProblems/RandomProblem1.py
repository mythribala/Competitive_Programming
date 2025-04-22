'''
Problem : Given a main string 's' and a list of strings 'wordsArray', Print the words from the 'wordsArray' 
which are subsequence of the main string 's'

Solution : Using Binary Search on Occurence Indices of each character

T.C : O(log(No. of words * No. of  characters in each word)) => O(log(n * m))
'''

#Code

from bisect import bisect_left

def check(word) :
    m = len(word)
    prevInd = -1
    for i in range(m) :
        curAlpha = word[i]
        curInd = bisect_left(occurInd[ord(curAlpha) - 97], prevInd + 1)
        if (curInd == leng[ord(curAlpha) - 97]) :
            return False
        else :
            prevInd = occurInd[ord(curAlpha) - 97][curInd]
    return True

s = input()
wordsArray = list(map(str, input().split()))

n = len(s)
occurInd = [[] for _ in range(26)]
for i in range(n) :
    occurInd[ord(s[i]) - 97].append(i)

leng = [len(occurInd[i]) for i in range(26)]

resWords = []
for word in wordsArray :
    if (check(word)) :
        resWords.append(word)
print(resWords)