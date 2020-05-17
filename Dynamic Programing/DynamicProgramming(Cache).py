#01123

def memoization():
    cache={} # here we have avoided global scope of variable
    def innerfunc(n):
        if n in cache:
            return cache[n]
        else:
            cache[n]=n+80
            print(f'first time of n is {n}')
            return cache[n]

    print(innerfunc)
    #Necessary to ruturn innerfunction without parentisis as we are telling the code to call the function type with that name
    return innerfunc
#011235
def fibonacciMemoization():
    cache={}
    def innerfunc(n):
        if n in cache:
            return cache[n]
        else:
            if n<2:
                return n
            else:
                cache[n]=innerfunc(n-1)+innerfunc(n-2)
                return cache[n]
    return innerfunc


mem=memoization()
print(mem(5))
print(mem(5))
print(mem(6))

fib=fibonacciMemoization()
print(fib(7))