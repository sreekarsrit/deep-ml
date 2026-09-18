def first_n_fibonacci(n):
    a:int=0;b:int=1
    fibo=[]
    if n<=0:
        return []
    elif n==1:
        return [0]
    else:
        fibo=[0,1]
        for i in range(2,n):
            a,b=b,a+b
            fibo.append(b)

    
    # Return a list of the first n Fibonacci numbers
    return fibo