#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int dx[] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[] = {1, -1, 0, 0, 1, -1, 1, -1};

void part1() {
    ifstream inputFile("input");
    vector<vector<char>> grid(140, vector<char>(140));
    for (int i=0; i<140; i++) {
        for (int j=0; j<140; j++) {
            inputFile >> grid[i][j];
        }
    }
    inputFile.close();

    int count=0;
    for (int i=0; i<140; i++) {
        for (int j=0; j<140; j++) {
            if (grid[i][j] == 'X') {
                for (int dir=0; dir<8; dir++) {
                    int x1 = i + dx[dir];
                    int y1 = j + dy[dir];
                    if (x1 >= 0 && x1 < 140 && y1 >= 0 && y1 < 140 && grid[x1][y1] == 'M') {
                        int x2 = x1 + dx[dir];
                        int y2 = y1 + dy[dir];
                        if (x2 >= 0 && x2 < 140 && y2 >= 0 && y2 < 140 && grid[x2][y2] == 'A') {
                            int x3 = x2 + dx[dir];
                            int y3 = y2 + dy[dir];
                            if (x3 >= 0 && x3 < 140 && y3 >= 0 && y3 < 140 && grid[x3][y3] == 'S') {
                                count++;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << count << endl;
}

void part2() {
    ifstream inputFile("input");
    vector<vector<char>> grid(140, vector<char>(140));
    for (int i=0; i<140; ++i) {
        for (int j=0; j<140; ++j) {
            inputFile >> grid[i][j];
        }
    }
    inputFile.close();

    int rows=140;
    int cols=140;
    int count=0;
    for (int i=1; i<rows-1; ++i) {
        for (int j=1; j<cols-1; ++j) {
            if (grid[i][j] == 'A') {
                char tl = grid[i-1][j-1];
                char tr = grid[i-1][j+1];
                char bl = grid[i+1][j-1];
                char br = grid[i+1][j+1];
                if ((tl == 'S' && tr == 'M' && bl == 'S' && br == 'M') ||
                    (tl == 'M' && tr == 'S' && bl == 'M' && br == 'S') ||
                    (tl == 'S' && tr == 'S' && bl == 'M' && br == 'M') ||
                    (tl == 'M' && tr == 'M' && bl == 'S' && br == 'S')) {
                    count++;
                }
            }
        }
    }
    cout << count << endl;
}

int main() {
    part1();
    part2();
    return 0;
}