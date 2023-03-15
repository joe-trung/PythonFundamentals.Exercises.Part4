def fibonnaci(n):
    if n<0 or n>30:
        return None
    elif n <= 1:
        return n
    else:
       return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(8))
    