import functools
import time

start1 = time.time()
def fib(n, memo = {0:0, 1:1}):
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
#print(fib(400))
end1 = time.time()    
print("func1 ", end1 - start1)

start2 = time.time()
@functools.lru_cache(None)
def fib2(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
#print(fib2(400))
end2 = time.time()
print("func2 ",end2 - start2)

start3 = time.time()
def fib3(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a
#print(fib3(9000))
end3 = time.time()
print("func3 ",end3 - start3)

start4 = time.time()
def fib4(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)
#print(fib4(20))
end4 = time.time()
print("func4 ",end4 - start4)

start5 = time.time()
def fib5(n):
    v1, v2, v3 = 1, 1, 0
    c=bin(n)    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
print(fib5(10))
end5 = time.time()
print("func5 ",end5 - start5)


