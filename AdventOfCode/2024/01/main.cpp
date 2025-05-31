#include <iostream>
#include "utils.h"
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

void part1(const vector<int>& col1, const vector<int>& col2) {
    vector<int> sortedCol1 = col1;
    vector<int> sortedCol2 = col2;

    sort(sortedCol1.begin(), sortedCol1.end());
    sort(sortedCol2.begin(), sortedCol2.end());

    int sumOfDifferences = 0;
    for (size_t i = 0; i < sortedCol1.size(); ++i) {
        sumOfDifferences += abs(sortedCol1[i] - sortedCol2[i]);
    }

    cout << "Sum of Differences: " << sumOfDifferences << endl;
}

void part2(const vector<int>& col1, const vector<int>& col2) {
    unordered_map<int, int> frequencyMap;
    for (const auto& num : col2) {
        frequencyMap[num]++;
    }

    int similarityScore = 0;
    for (const auto& num : col1) {
        similarityScore += num * frequencyMap[num];
    }

    cout << "Similarity Score: " << similarityScore << endl;
}

int main() {
    vector<string> lines = Utils::readFile("input");
    vector<int> col1, col2;

    for (const auto& line : lines) {
        auto tokens = Utils::split(Utils::trim(line));
        if (tokens.size() >= 2) {
            col1.push_back(stoi(tokens[0]));
            col2.push_back(stoi(tokens[1]));
        }
    }

    cout << "Part 1:" << endl;
    part1(col1, col2);

    cout << "Part 2:" << endl;
    part2(col1, col2);

    return 0;
}