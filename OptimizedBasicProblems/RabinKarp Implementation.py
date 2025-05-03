'''

Rabin Karp -> String Matching Algorithm

'''

class rabinKarp:

    def __init__(self, s, base, mod1, mod2) :
        self.rhash1 = [0]
        self.rhash2 = [0]
        self.power1 = [1]
        self.power2 = [1]
        self.mod1 = mod1
        self.mod2 = mod2
        for alpha in s :
            self.rhash1.append(((self.rhash1[-1] * base % mod1) + (ord(alpha) - 97) + mod1) % mod1)
            self.rhash2.append(((self.rhash2[-1] * base % mod2) + (ord(alpha) - 97) + mod2) % mod2)
            self.power1.append(self.power1[-1] * base % mod1)
            self.power2.append(self.power2[-1] * base % mod2)

    def getHash(self, l, r) :
        hash1 = (self.rhash1[r + 1] - (self.rhash1[l] * self.power1[r - l + 1] % self.mod1)) % self.mod1
        hash2 = (self.rhash2[r + 1] - (self.rhash2[l] * self.power2[r - l + 1] % self.mod2)) % self.mod2
        return (hash1, hash2)

s = input()
t = input()
n = len(s)
m = len(t)

mod1 = pow(10, 9) + 7
mod2 = pow(10, 9) + 9
pattHash = rabinKarp(t, 367, mod1, mod2)
strHash = rabinKarp(s, 367, mod1, mod2)
needHash = pattHash.getHash(0, m - 1)
idx = -1
for i in range(n) :
    if (i + m - 1 >= n) :
        break
    curHash = strHash.getHash(i, i + m - 1)
    if (curHash == needHash) :
        idx = i
        break
print(idx)
