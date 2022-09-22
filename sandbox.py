from functools import cache
import math
import time

def my_cache(func):
    memo = {}
    def wrapper(*args):
        if tuple(args) not in memo:
            print(tuple(args))
            memo[tuple(args)] = func(*args)
        return memo[tuple(args)]
    return wrapper


@cache
def primes(n):
    primes = [2]
    for i in range(3,n+1,2):
        for prime in primes:
            if i % prime == 0 :
                break
        else:
            primes.append(i)
    return primes


def inc_fib(n):
    cnt = 0
    a, b = 0, 1
    while cnt<n:
        a, b = b, a + b
        cnt+=1
    return a


@cache
def rec_fib(n):
    if(n<=1):
        return n
    return rec_fib(n-1) + rec_fib(n-2)

@my_cache
def approx_pi(n):
    res = 0
    for i in range(n):
        res += 4/(2.0*i+1)*(-1)**i
    return res

def bad_prime(n):
    res = []
    i = 1
    while(i < n):
        i+=1
        for g in range(2,i-1):
            if i%g == 0:
                break
        else:
            res.append(i)
    return res

def count_time(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        return (func.__name__, end-start, len(res))
    return wrapper





def diff_equals_self(n):
    rat = 100
    rai = 0
    for i in range(1,n):
        for j in range(i+1, n):
            s = str(sums(j) - sums(i-1))
            if s == str(i)+str(j) or s == str(j)+str(i):
                rat = min(rat, j/i)
                rai = max(rai, j/i)
                print(i,j, s)
    print(rat, rai)
    return None


#APPROX FOR FIB SEQUENCE
c = 1/(math.sqrt(5))
c1, c2 = (1+math.sqrt(5))/2, (1-math.sqrt(5))/2

miny = 100
for i in range(1,1000):
    approx = c*(c1**i) - c*(c2**i)
    actual = rec_fib(i) 
    miny = min(miny,(actual- approx)/actual)
print(miny)
