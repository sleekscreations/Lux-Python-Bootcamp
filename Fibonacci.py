# creating a function that checks whether a number belongs to the Fibonucci sequence or not

def recur_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

n_terms = 15


if n_terms <= 0:
   print("Plese enter a number greater than or equals to 0")
else:
   print("Fibonacci sequence:")
   for i in range(n_terms):
       print(recur_fibonacci(i))

