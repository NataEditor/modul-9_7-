
    
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % result == 0 and result != 0:
            print('Простое')
        else:
            print('Составное')
    return wrapper


@is_prime
def sum_three(a,b,c):
    d=a+b+c
    print(d)
    return d


result = sum_three(2, 3, 6)


