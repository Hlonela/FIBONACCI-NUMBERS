def fib2(n): # Created a function to return fibonacci numbers
    if n==0: # if n is 0, the program must return 0
        return 0
    if n==1 or n==2: # If n is 1 or 2, the answer will be the same (answer = 1)
        return 1
    else:
        return fib2(n-1) + fib2(n-2) #If n is greater than 2, then the program can start adding the two numbers infront
n=20
for x in range(1, n): # The range means that the program should start from 1 until the nth number which happens to be twenty.
    print(fib2(x), end = " ") # Each digit must be printed next to each other and not below one number
