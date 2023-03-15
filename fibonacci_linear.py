def fibonacci_linear(n):
    if n<0:
        return None
    elif n<1:
        return n
    else:
        fibo0 = 1
        fibo1 = 1
        fibo2 = fibo0 + fibo1
        for i in range(2,n-1):
             fibo0 =fibo1
             fibo1 =fibo2
             fibo2=fibo0 +fibo1
        return fibo2


print(fibonacci_linear(11))