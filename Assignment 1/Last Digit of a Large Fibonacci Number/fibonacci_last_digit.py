# Uses python3
import sys
import numpy as np

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


# its found that the last number of fibonacci number has a sequence that
# is repeated every 60 number, for example
# Fib(n) - > 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
# LastDigit(n) -> 0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7
# so all we need to compute is these 60 numbers, store them in an array and 
# when a number comes all we have tto do is to random access the array with index = number mod 60 to
# find its position and return this number which gives us the solution in O(1)

def last_digit_of_fib(n):

    # create the 60 repeated sequence of last digit
    fib_rep_60_seq = [0] * 61;

    # first two numbers of the sequence = 0,1
    fib_rep_60_seq[0] = 0;
    fib_rep_60_seq[1] = 1;

    # loop from 2 to 61 to store the sequence 
    for i in range(2, 61):
        fib_rep_60_seq[i] = (fib_rep_60_seq[i - 1] + fib_rep_60_seq[i - 2]) % 10;

    # find last digit with the number mod 60
    return fib_rep_60_seq[n % 60]




# def stress_test(n):
#     numbers = np.random.randint(0,10000,size=n)
#     return numbers

if __name__ == '__main__':

    input = sys.stdin.readline()
    n = int(input)
    print(last_digit_of_fib(n))

    # input = stress_test(1000)
    # for i in range(len(input)):
    #     my_value = last_digit_of_fib(input[i])
    #     expected = get_fibonacci_last_digit_naive(input[i])
    #     if (expected - my_value)%10 != 0:
    #         print("error at "+str(input[i]))
    #         break;
    # print('Tests Ran Successfully')
