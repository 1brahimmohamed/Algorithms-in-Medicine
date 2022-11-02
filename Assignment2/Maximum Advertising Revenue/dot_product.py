#Uses python3

import sys

def max_dot_product(a, b):

    # write your code here

    # sort the two arrays using bubble sort 
    for i in range(len(a)):

        # flag for swapping
        swapped =  False

        for j in range(0, len(a)-i-1):
            
            #------------------------ Sorting Array a -----------------------#

            # swap the element of array a if it's larger than the next element
            if a[j] > a[j+1]:

                # make the swap
                a[j], a[j+1] = a[j+1], a[j]

                # set the flag swapped to true
                swapped = True


            #------------------------ Sorting Array b -----------------------#
            
            # swap the element of array b if it's larger than the next element
            if b[j] > b[j+1]:

                # make the swap
                b[j], b[j+1] = b[j+1], b[j]

                # set the flag swapped to true
                swapped = True
        
        # break the loop if there is no swapped elements
        # this is for optimizing the bubble sort to give better results,
        # if the array is sorted so we don't do the operation in O(N^2)
        if swapped == False:
            break
    
    # result of dot product
    res = 0

    # multiply each element in a with the corresponding element in b to
    # maximize the dot product
    for i in range(n):
        res += a[i] * b[i]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
