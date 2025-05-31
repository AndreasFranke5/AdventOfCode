#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include "utils.h"

using namespace std;

void part1() {
    int safeRow = 0;
    string line;

    ifstream infile("input");
    if (!infile.is_open()) {
        cerr << "Error: Couldn't open file" << endl;
        return;
    }

    while (getline(infile, line)) {
        line = Utils::trim(line);
        if (line.empty()) continue;

        vector<string> tokens = Utils::split(line);
        vector<int> nums = Utils::stringsToInts(tokens);

        bool isSorted=true;
        bool maxDiffOk=true;
        bool noAdjacentIdentical=true;
        bool ascending = nums[1] >= nums[0];

        if (nums.size()>=2) {
            for (size_t i=1; i<nums.size(); ++i) {
                if (ascending) {
                    if (nums[i] < nums[i-1]) {
                        isSorted=false;
                        break;
                    }
                } else { // Descending
                    if (nums[i] > nums[i-1]) {
                        isSorted=false;
                        break;
                    }
                }
                if (abs(nums[i] - nums[i-1]) > 3) { // 3 is max difference
                    maxDiffOk=false;
                    break;
                }
                if (nums[i] == nums[i-1]) { // No adjacent identical values
                    noAdjacentIdentical=false;
                    break;
                }
            }
        }

        if (isSorted && maxDiffOk && noAdjacentIdentical) {
            safeRow++;
        }
    }

    cout << safeRow << endl;
}

void part2() {
    int safeRow = 0;
    string line;

    ifstream infile("input");
    if (!infile.is_open()) {
        cerr << "Error: Could not open input file" << endl;
        return;
    }

    while (getline(infile, line)) {
        line = Utils::trim(line);
        if (line.empty()) continue;

        vector<string> tokens=Utils::split(line);
        vector<int> nums=Utils::stringsToInts(tokens);

        auto checkConditions=[](const vector<int>& nums) -> bool {
            if (nums.size()<2) {
                return true;
            }

            bool isSorted=true;
            bool maxDiffOk=true;
            bool noAdjacentIdentical=true;
            bool ascending=nums[1]>=nums[0];

            for (size_t i=1; i<nums.size(); ++i) {
                if (ascending) {
                    if (nums[i] < nums[i-1]) {
                        isSorted=false;
                        break;
                    }
                } else { // Descending
                    if (nums[i] > nums[i-1]) {
                        isSorted=false;
                        break;
                    }
                }

                if (abs(nums[i] - nums[i-1]) > 3) { // 3 is max difference
                    maxDiffOk=false;
                    break;
                }

                if (nums[i] == nums[i-1]) { // No adjacent identical values
                    noAdjacentIdentical=false;
                    break;
                }
            }

            return isSorted && maxDiffOk && noAdjacentIdentical;
        };

        // Check if original row is safe before starting to remove elements
        if (checkConditions(nums)) {
            safeRow++;
            continue;
        }

        // Remove each element to see if row can be made safe
        bool canBeMadeSafe = false;
        for (size_t i=0; i<nums.size(); ++i) {
            vector<int> modifiednums=nums;
            modifiednums.erase(modifiednums.begin() + i);

            if (checkConditions(modifiednums)) {
                canBeMadeSafe = true;
                break;
            }
        }

        if (canBeMadeSafe) {
            safeRow++;
        }
    }

    cout << safeRow << endl;
}

int main() {
    part1();
    part2();
    return 0;
}