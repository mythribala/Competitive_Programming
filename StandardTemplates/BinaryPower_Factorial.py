def modExp(base, power, mod) :
    res = 1
    base %= mod 
    while (power > 0) :
        if (power % 2) :
            res = (res * base) % mod 
        base = (base * base) % mod 
        power //= 2
    return res

def precomputeFact(n, mod) :
    fact = [1] * (n + 1)
    for i in range(2, n + 1) :
        fact[i] = (fact[i - 1] * i) % mod  

    invFact = [1] * (n + 1)
    invFact[n] = modExp(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1) :
        invFact[n] = (invFact[i + 1] * (i + 1)) % mod 

    return fact, invFact

def nCr(n, r, p) :
    if (r < 0 or r > n) :
        return 0
    return ((fact[n] % mod) * (invFact[r] % p) * (invFact[n - r] % p)) % p 

'''

Similarly, Matrix Exponentiation : matrix A ^ N

res = Identity matrix of size (col * col)
while (N > 0) :
  if (N % 2) :
    res = matMul(A, res) #where matMul implements the matrix multiplication in p*q*r time complexity
  A = matMul(A, A) 
  N //= 2
return res

'''