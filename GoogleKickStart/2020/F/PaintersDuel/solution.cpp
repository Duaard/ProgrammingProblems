#include <bits/stdc++.h>

using namespace std;

struct position
{
    int r;
    int p;
};

void showGrid(vector<vector<int>> grid, position a, position b)
{
    grid[a.r][a.p] = 2;
    grid[b.r][b.p] = 3;
    for (auto row : grid)
    {
        for (auto col : row)
        {
            cout << col << " ";
        }
        cout << "\n";
    }
}

bool gameEnd(vector<vector<int>> grid, position a, position b, int turn)
{
    // Check if there are still available moves
    position player = turn ? b : a;
    bool end = true;

    // Horizontal movement
    if (grid[player.r][player.p - 1] || grid[player.r][player.p + 1])
    {
        end = false;
    }
    // Vertical movement
    bool p_even = (player.r + player.p) % 2 == 0;
    bool s_even = grid.size() % 2 == 0;
    bool up = p_even == s_even;
    if ((up && grid[player.r - 1][player.p]) || (!up && grid[player.r + 1][player.p]))
    {
        end = false;
    }

    return end;
}

int getScore(vector<vector<int>> grid, position a, position b, int turn, int curScore)
{
    position player;
    position *playerPntr;

    player = turn ? b : a;
    playerPntr = turn ? &b : &a;

    bool p_even = (player.r + player.p) % 2 == 0;
    bool s_even = grid.size() % 2 == 0;

    // Do the 3 possible movements
    int move = turn ? curScore - 1 : curScore + 1;
    int n_turn = turn ? 0 : 1;

    int worst = turn ? 1e5 : -1e5;

    int l = worst, r = worst, u = worst, d = worst, s = worst;

    // Move left
    if (grid[player.r][player.p - 1])
    {
        grid[player.r][player.p - 1] = 0;
        playerPntr->p -= 1;
        l = getScore(grid, a, b, n_turn, move);
        grid[player.r][player.p - 1] = 1;
        playerPntr->p += 1;
    }
    // Move right
    if (grid[player.r][player.p + 1])
    {
        grid[player.r][player.p + 1] = 0;
        playerPntr->p += 1;
        r = getScore(grid, a, b, n_turn, move);
        grid[player.r][player.p + 1] = 1;
        playerPntr->p -= 1;
    }
    // Move up
    bool up = p_even == s_even;

    if (up && grid[player.r - 1][player.p])
    {
        grid[player.r - 1][player.p] = 0;
        playerPntr->r -= 1;
        u = getScore(grid, a, b, n_turn, move);
        grid[player.r - 1][player.p] = 1;
        playerPntr->r += 1;
    }
    // Move down
    if (!up && grid[player.r + 1][player.p])
    {
        grid[player.r + 1][player.p] = 0;
        playerPntr->r += 1;
        d = getScore(grid, a, b, n_turn, move);
        grid[player.r + 1][player.p] = 1;
        playerPntr->r -= 1;
    }

    // If this player doesn't have any more moves
    // But the opponent can still move
    if (gameEnd(grid, a, b, turn) && !gameEnd(grid, a, b, n_turn))
    {
        // cout << "STAYING!!!\n";
        s = getScore(grid, a, b, n_turn, curScore);
    }

    // If there's no more move for any players
    if (gameEnd(grid, a, b, turn) && gameEnd(grid, a, b, n_turn))
    {
        return curScore;
    }

    // Return best score possible
    if (turn)
    {
        // Minimize score
        return min({l, r, u, d, s});
    }
    else
    {
        // Maximize score
        return max({l, r, u, d, s});
    }
}

void solve()
{
    int s, r_a, p_a, r_b, p_b, c;

    cin >> s >> r_a >> p_a >> r_b >> p_b >> c;

    position a_pos, b_pos;
    a_pos = {r_a, p_a + (s - r_a)};
    b_pos = {r_b, p_b + (s - r_b)};

    vector<position> c_pos(c);

    for (int i = 0; i < c; i++)
    {
        cin >> c_pos[i].r >> c_pos[i].p;
    }

    int row = s + 2,
        col = (s * 2) + 1;

    vector<vector<int>> grid(row, vector<int>(col));
    int val = 0;
    // Create the grid
    for (int i = 0; i < row; i++)
    {
        int rooms = (i * 2) - 1;
        for (int j = 0; j < col; j++)
        {
            val = 0;
            if ((j > s - i) && rooms)
            {
                val = 1;
                rooms--;
            }
            if (i == 0 || i == row - 1)
            {
                val = 0;
            }
            grid[i][j] = val;
        }
    }

    // Disregard c rooms
    for (int i = 0; i < c; i++)
    {
        int r = c_pos[i].r, p = c_pos[i].p;
        p = p + (s - r);
        grid[r][p] = 0;
    }

    // Mark start pos as 0
    grid[a_pos.r][a_pos.p] = 0;
    grid[b_pos.r][b_pos.p] = 0;

    // showGrid(grid, a_pos, b_pos);
    // cout << "GET SCORE\n";

    int score = getScore(grid, a_pos, b_pos, 0, 0);

    cout << score << "\n";
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}