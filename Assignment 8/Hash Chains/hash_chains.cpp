#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using std::string;
using std::vector;
using std::cin;

struct Query {
    string type, s;
    size_t ind;
};

class QueryProcessor {
    int bucket_count;

    // store all lists of strings in one vector
    vector<std::list<string>> elems;

    // polynomial hash function
    size_t hash_func(const string &s) const {
        static const size_t multiplier = 263;
        static const size_t prime = 1000000007;
        unsigned long long hash = 0;
        for (int i = static_cast<int> (s.size()) - 1; i >= 0; --i)
            hash = (hash * multiplier + s[i]) % prime;
        return hash % bucket_count;
    }

public:
    // constructor
    explicit QueryProcessor(int bucket_count) {
        this->bucket_count = bucket_count;       // initialize the number of buckets
        elems.resize(bucket_count);      // resize the vector to the number of buckets
    }

    Query readQuery() const {
        Query query;
        cin >> query.type;                      // read the type of query
        if (query.type !=
            "check")              // if the query is not "check" then it is "find" or "add" or "del" so read the string
            cin >> query.s;
        else
            cin >> query.ind;                   // if the query is "check" then read the index to check
        return query;
    }

    void writeSearchResult(bool was_found) const {
        std::cout << (was_found ? "yes\n" : "no\n");            // ternary operator to print "yes" or "no"
    }

    void processQuery(const Query &query) {

        // if the query is "check" then print the list at the index
        if (query.type == "check") {

            // check if the index is valid and inside our vector
            if (query.ind < elems.size()) {

                // loop on te lists in the vector at the index
                for (auto s: elems[query.ind]) {
                    std::cout << s << " ";
                }
                std::cout << "\n";
            }
        } else {

            // if the query is "find" or "add" or "del" then get the hash value of the string
            size_t hash_idx = hash_func(query.s);

            // create an iterator to loop on the list at the index
            auto it = std::find(elems[hash_idx].begin(), elems[hash_idx].end(), query.s);

            // if the query is "find" then print "yes" if the string is found and "no" if not
            if (query.type == "find")
                writeSearchResult(it != elems[hash_idx].end());

                // if the query is "add" then add the string to the list at the index if it is not found
            else if (query.type == "add") {
                if (it == elems[hash_idx].end())
                    elems[hash_idx].push_front(query.s);
            }

                // if the query is "del" then delete the string from the list at the index if it is found
            else if (query.type == "del") {
                if (it != elems[hash_idx].end())
                    elems[hash_idx].erase(it);
            }
        }
    }

    void processQueries() {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            processQuery(readQuery());
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    int bucket_count;
    cin >> bucket_count;
    QueryProcessor proc(bucket_count);
    proc.processQueries();
    return 0;
}
