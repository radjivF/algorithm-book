fibTable = {1:1, 2:1}
def fib(n):
   if n <= 2:
      return 1
   if n in fibTable:
      return fibTable[n]
   else:
      fibTable[n] = fib(n-1) + fib(n-2)
      return fibTable[n]
