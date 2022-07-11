import math
import time


def find_primes(n):
    file = open("primes.txt", "w")
    data = []
    start_time = time.time()
    counter = 1
    primes = [2]
    i = 3
    while(counter < n):
        for prime in primes:
            if i % prime == 0 :
                break
        else:
            primes.append(i)
            data.append( (counter+1,time.time() - start_time) )
            if(counter+1) % 100 == 0:
                file.write("\n{:.0f}, {:.10f}".format(counter+1, time.time() - start_time))
            counter += 1
        i+=2
    return data

d = find_primes(100000)
