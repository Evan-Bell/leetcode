import math
import time

def my_cache(func):
    memo = {}
    def wrapper(*args):
        if tuple(args) not in memo:
            memo[tuple(args)] = func(*args)
        return memo[tuple(args)]
    return wrapper


@my_cache
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

@my_cache
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

# print(primes(1000))
# print(inc_fib(10))
#rec_fib(40)
print(approx_pi(10000000))


