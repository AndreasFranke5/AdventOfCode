#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

class Utils {
public:
    // Function to read an entire file line by line
    static vector<string> readFile(const string& filename) {
        vector<string> lines;
        ifstream infile(filename);
        string line;
        while (getline(infile, line)) {
            lines.push_back(line);
        }
        return lines;
    }

// Function to split a string by spaces
static vector<string> split(const string& str) {
    vector<string> tokens;
    istringstream tokenStream(str);
    string token;
    while (tokenStream >> token) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to convert a vector of strings to a vector of integers
static vector<int> stringsToInts(const vector<string>& strVec) {
    vector<int> intVec;
    for (const string& s : strVec) {
        string trimmed = trim(s);
        if (!trimmed.empty()) {
            try {
                int num = stoi(trimmed);
                intVec.push_back(num);
            } catch (const invalid_argument& e) {
                cerr << "Warning: Invalid integer '" << trimmed << "' encountered. Skipping." << endl;
                // Optionally, you can choose to handle the error differently
            } catch (const out_of_range& e) {
                cerr << "Warning: Integer '" << trimmed << "' out of range. Skipping." << endl;
            }
        }
    }
    return intVec;
}

    // Function to trim whitespace from a string (leading and trailing)
    static string trim(const string& str) {
        size_t first = str.find_first_not_of(" \t");
        if (first == string::npos) return ""; // All whitespace
        size_t last = str.find_last_not_of(" \t");
        return str.substr(first, (last - first + 1));
    }
};

#endif
