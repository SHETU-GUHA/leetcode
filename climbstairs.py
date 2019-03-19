def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
def countWays(x):
    return fib(x + 1)

x = 3
print ("Number of ways: ",countWays(x)),

