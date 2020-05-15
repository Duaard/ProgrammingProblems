#include <bits/stdc++.h>
using namespace std;

int domino(int m, int n)
{
    return m * n / 2;
}

int main()
{
    int m, n;
    cin >> m >> n;
    cout << domino(m, n) << "\n";
    return 0;
}