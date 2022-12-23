#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;

class HeapBuilder {
private:
    vector<int> data_;
    vector<pair<int, int> > swaps_;

    void WriteResponse() const {
        cout << swaps_.size() << "\n";
        for (int i = 0; i < swaps_.size(); ++i) {
            cout << swaps_[i].first << " " << swaps_[i].second << "\n";
        }
    }

    void ReadData() {
        int n;
        cin >> n;
        data_.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> data_[i];
    }

    void siftDown(int i){
        // minimum index = current index

        int min = i;                                        // root index (should be less than l & r)
        int l = (2*i + 1);                                  // the left node is equal to the element in index 2i+1
        int r = (2*i + 2);                                  // the left node is equal to the element in index 2i+2

        // if the left child is less than the min then the new min = the left child
        if(l <= data_.size()-1 && data_[l] < data_[min])
            min = l;

        // if the right child is less than the min then the new min = the right child
        if(r <= data_.size()-1 && data_[r] < data_[min])
            min = r;

        /** if the min index not equal the index we started with
         * therefore a swap needs to be done
        **/
        if(min != i){
            swap(data_[i], data_[min]);             // make the sawp
            swaps_.push_back(make_pair(i, min));     // push the swap pair to the swaps vector
            siftDown(min);                              // call siftDown again until this part of the tree is heapified
        }
    }
    void GenerateSwaps() {
        swaps_.clear();
        // The following naive implementation just sorts
        // the given sequence using selection sort algorithm
        // and saves the resulting sequence of swaps.
        // This turns the given array into a heap,
        // but in the worst case gives a quadratic number of swaps.
        //
        // TODO: replace by a more efficient implementation

        // loop starts from half number of the elements of the array - 1
        for(int i = ((data_.size())/2) - 1; i >= 0; i--){
            siftDown(i);
        }
    }


public:
    void Solve() {
        ReadData();
        GenerateSwaps();
        WriteResponse();
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    HeapBuilder heap_builder;
    heap_builder.Solve();
    return 0;
}
