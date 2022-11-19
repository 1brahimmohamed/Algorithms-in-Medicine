#include <iostream>
#include <vector>

using std::vector;

int lcs2(vector<int> &a, vector<int> &b) {
    
    // get the size of the two vectors (words)
    size_t sizeOfA = a.size();
    size_t sizeofB = b.size();

    // create table of integers (2d vector/array) with the size of the two words
    vector<vector<int>> lcsTable(sizeOfA + 1,vector<int>(sizeofB + 1));

    // loop in the 2 words
    for (int i = 0; i <= sizeOfA; i++)
    {
        for (int j = 0; j <= sizeofB; j++)
        {
            // make the first row and first column equal to zeros in the table
            if (i == 0 || j == 0)
                lcsTable[i][j] = 0;

            // if the two values matches, then add 1 to the value of the diagonal (upper left cell)
            else if (a[i - 1] == b[j - 1])
                lcsTable[i][j] = lcsTable[i - 1][j - 1] + 1;

            // if they do not match, then take the maximum of the left cell & the upper cell
            else
                lcsTable[i][j] = std::max(lcsTable[i - 1][j], lcsTable[i][j - 1]);
        }
    }

    // return the last cell of the table which contains the largest number
    return lcsTable[sizeOfA][sizeofB];
}

int main() {
  size_t n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> a[i];
  }

  size_t m;
  std::cin >> m;
  vector<int> b(m);
  for (size_t i = 0; i < m; i++) {
    std::cin >> b[i];
  }

  std::cout << lcs2(a, b) << std::endl;
}
