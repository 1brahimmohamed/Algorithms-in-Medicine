#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    if (dist <= tank)
        return 0;

    int numberOfStops = 0;
    int currentStop = 0;
    int distanceCovered = 0;
    bool flag = false;

    stops.push_back(dist);
    int i = 0;

    while (distanceCovered < dist) {
        while (i < stops.size() and stops[i] - currentStop <= tank) {
            i++;
            flag = true;
        }
        if (flag) {
            if (i == stops.size()) break;
            currentStop = stops[i - 1];
            distanceCovered = currentStop;
            numberOfStops += 1;
        } else {
            return -1;
        }
        flag = false;
    }
    return numberOfStops;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
