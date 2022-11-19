# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_number_of(n):

    # if n = 1 or 0 return 1
    if n <=1:
        return n
    else:
        # store first 2 numbers in the array
        fib = [0,1]
        for i in range(n-1):
            temp = fib[1]
            fib[1] = fib[0] + fib[1]
            fib[0] = temp
        return fib[1] 

def get_fibonacci_huge_fast(n, m):

    # getting the pisano period of the code 
    previous, current = 0, 1
    pis_period = 0 
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # if period starts with 0 1
        if (previous == 0 and current == 1):
            pis_period = i + 1
    
    # get the mod of n with the period
    n_mod_period = n % pis_period

    # get the fibonacci number of the number mod period
    Fn = get_fibonacci_number_of(n_mod_period)
    return Fn % m

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
