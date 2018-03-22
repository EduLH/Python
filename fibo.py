import time

start = time.time()

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(894651))

end = time.time()

elapsed = end - start
print ("tempo percorrido de:")
print (elapsed)
