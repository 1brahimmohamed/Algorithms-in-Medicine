#include <algorithm>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using std::vector;

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}


long long max_dot_product(vector<int> a, vector<int> b) {
    // write your code here

    // flag for swapping
    bool swapped;

    // sort the two arrays using bubble sort
    for (int i = 0; i < a.size() - 1; i++) {
        swapped = false;

        //------------------------ Sorting Array a -----------------------//

        // swap the element of array a if it's larger than the next element
        for (int j = 0; j < b.size() - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);        // make the swap
                swapped = true;                   // set the flag swapped to true
            }

        //------------------------ Sorting Array a -----------------------//

        //swap the element of array b if it's larger than the next element
            if (b[j] > b[j + 1]) {
                swap(b[j], b[j + 1]);       // make the swap
                swapped = true;                   // set the flag swapped to true
            }
        }

        /*
         * break the loop if there is no swapped elements
         * this is for optimizing the bubble sort to give better results,
         * if the array is sorted so we don't do the operation in O(N^2)
         */

        if (!swapped)
            break;
    }

    // result of dot product
    long long result = 0;
    for (size_t i = 0; i < a.size(); i++) {
        result += ((long long) a[i]) * b[i];
    }
    return result;
}

int main() {
    size_t n;
    std::cin >> n;
    vector<int> a(n), b(n);
    for (size_t i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    for (size_t i = 0; i < n; i++) {
        std::cin >> b[i];
    }
    std::cout << max_dot_product(a, b) << std::endl;
}
