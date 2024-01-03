#serie de fibonacci entre el 0 y el número dado

def fibonacci(num):
    serie_fib=[0]
    a,b=0,1
    for i in range(num):
        if b > num : 
            return serie_fib
        else: 
            serie_fib.append(b)
            a,b = b, a+b

resultado=fibonacci(2023)

print(resultado)