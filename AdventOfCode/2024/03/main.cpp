#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

void part1() {
    ifstream infile("input");
    if (!infile.is_open()) {
        cerr << "Error: Couldn't open file" << endl;
        return;
    }

    string content;
    string line;
    while (getline(infile, line)) {
        content+=line;
    }
    long long total=0;
    size_t pos=0;
    auto npos=std::string::npos;
    while ((pos=content.find("mul(", pos)) != npos) {
        pos += 4;
        string n1s;
        string n2s;
        while (pos < content.size() && isdigit(content[pos])) {
            n1s += content[pos];
            pos++;
        }
        if (pos >= content.size() || content[pos] != ',') {
            continue;
        }
        pos++;
        while (pos < content.size() && isdigit(content[pos])) {
            n2s += content[pos];
            pos++;
        }
        if (pos >= content.size() || content[pos] != ')') {
            continue;
        }
        pos++;
        int n1=stoi(n1s);
        int n2=stoi(n2s);
        total += static_cast<long long>(n1) * n2;
    }
    cout << total << endl;
}

void part2() {
    ifstream infile("input");
    if (!infile.is_open()) {
        cerr << "Error: Couldn't open file" << endl;
        return;
    }

    string content;
    string line;
    while (getline(infile, line)) {
        content+=line;
    }

    long long total=0;
    size_t pos=0;
    bool mul_on=true;

    while (pos<content.size()) {
        if (content.compare(pos, 4, "do()") == 0) {
            mul_on=true;
            pos += 4;
            continue;
        }
        if (content.compare(pos, 7, "don't()") == 0) {
            mul_on=false;
            pos += 7;
            continue;
        }
        if (mul_on && content.compare(pos, 4, "mul(") == 0) {
            pos += 4;
            string n1s;
            string n2s;
            while (pos<content.size() && isdigit(content[pos])) {
                n1s += content[pos];
                pos++;
            }
            if (pos >= content.size() || content[pos] != ',') {
                continue;
            }
            pos++;
            while (pos<content.size() && isdigit(content[pos])) {
                n2s += content[pos];
                pos++;
            }
            if (pos >= content.size() || content[pos] != ')') {
                continue;
            }
            pos++;
            int n1=stoi(n1s);
            int n2=stoi(n2s);
            total += static_cast<long long>(n1) * n2;
        } else {
            pos++;
        }
    }
    cout << total << endl;
}

int main() {
    part1();
    part2();
    return 0;
}