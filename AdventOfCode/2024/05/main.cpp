#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

void part1() {
    ifstream fin1("input1");
    if (!fin1.is_open()) {
        cerr << "Error: Couldn't open file (input1)" << endl;
        return;
    }
    unordered_map<int, unordered_set<int>> sortRules;
    string line;
    while (getline(fin1, line)) {
        size_t bar_pos=line.find('|');
        if (bar_pos==string::npos) continue;
        int x=stoi(line.substr(0, bar_pos));
        int y=stoi(line.substr(bar_pos+1));
        sortRules[x].insert(y);
    }
    fin1.close();
    ifstream fin2("input2");
    if (!fin2.is_open()) {
        cerr << "Error: Couldn't open file (input2)" << endl;
        return;
    }
    vector<vector<int>> upds;
    while (getline(fin2, line)) {
        vector<int> upd;
        size_t pos=0;
        while (pos<line.size()) {
            size_t commaPos=line.find(',', pos);
            string numStr;
            if (commaPos==string::npos) {
                numStr=line.substr(pos);
                pos=line.size();
            } else {
                numStr=line.substr(pos, commaPos-pos);
                pos=commaPos+1;
            }
            numStr.erase(0, numStr.find_first_not_of(' '));
            numStr.erase(numStr.find_last_not_of(' ')+1);
            upd.push_back(stoi(numStr));
        }
        upds.push_back(upd);
    }
    fin2.close();
    int tot=0;
    for (const auto &upd : upds) {
        unordered_map<int, int> pagepos;
        for (size_t i=0;i<upd.size();++i) {
            pagepos[upd[i]]=i;
        }
        bool valid=true;
        for (const auto &rule : sortRules) {
            int x=rule.first;
            for (int y : rule.second) {
                if (pagepos.count(x) && pagepos.count(y)) {
                    if (pagepos[x] >= pagepos[y]) {
                        valid=false;
                        break;
                    }
                }
            }
            if (!valid) break;
        }
        if (valid && !upd.empty()) {
            int midIdx=upd.size()/2;
            int midPg=upd[midIdx];
            tot+=midPg;
        }
    }
    cout << tot << endl;
}

void part2() {
    ifstream fin1("input1");
    if (!fin1.is_open()) {
        cerr << "Error: Couldn't open file (input1)" << endl;
        return;
    }
    unordered_map<int, unordered_set<int>> sortRules;
    string line;
    while (getline(fin1, line)) {
        size_t bar_pos=line.find('|');
        if (bar_pos==string::npos) continue;
        int x=stoi(line.substr(0, bar_pos));
        int y=stoi(line.substr(bar_pos+1));
        sortRules[x].insert(y);
    }
    fin1.close();
    ifstream fin2("input2");
    if (!fin2.is_open()) {
        cerr << "Error: Couldn't open file (input2)" << endl;
        return;
    }
    vector<vector<int>> upds;
    while (getline(fin2, line)) {
        vector<int> upd;
        size_t pos=0;
        while (pos<line.size()) {
            size_t commaPos=line.find(',', pos);
            string numStr;
            if (commaPos==string::npos) {
                numStr=line.substr(pos);
                pos=line.size();
            } else {
                numStr=line.substr(pos, commaPos-pos);
                pos=commaPos+1;
            }
            numStr.erase(0, numStr.find_first_not_of(' '));
            numStr.erase(numStr.find_last_not_of(' ')+1);
            upd.push_back(stoi(numStr));
        }
        upds.push_back(upd);
    }
    fin2.close();
    int tot=0;
    for (const auto &upd : upds) {
        unordered_map<int, int> pagepos;
        for (size_t i=0;i<upd.size();++i) {
            pagepos[upd[i]]=i;
        }
        bool valid=true;
        for (const auto &rule : sortRules) {
            int x=rule.first;
            for (int y : rule.second) {
                if (pagepos.count(x) && pagepos.count(y)) {
                    if (pagepos[x] >= pagepos[y]) {
                        valid=false;
                        break;
                    }
                }
            }
            if (!valid) break;
        }
        if (!valid && !upd.empty()) {
            unordered_map<int, unordered_set<int>> graph;
            unordered_map<int, int> indeg;
            unordered_set<int> upd_pg_amt(upd.begin(), upd.end());
            for (const auto &rule : sortRules) {
                int x=rule.first;
                for (int y : rule.second) {
                    if (upd_pg_amt.count(x) && upd_pg_amt.count(y)) {
                        graph[x].insert(y);
                        indeg[y]++;
                        if (indeg.find(x)==indeg.end()) {
                            indeg[x]=0;
                        }
                    }
                }
            }
            for (int page : upd_pg_amt) {
                if (indeg.find(page)==indeg.end()) {
                    indeg[page]=0;
                }
            }
            queue<int> q;
            for (const auto &entry : indeg) {
                if (entry.second==0) {
                    q.push(entry.first);
                }
            }
            vector<int> sort_upd;
            while (!q.empty()) {
                int node=q.front();
                q.pop();
                sort_upd.push_back(node);
                if (graph.count(node)) {
                    for (int neighbor : graph[node]) {
                        indeg[neighbor]--;
                        if (indeg[neighbor]==0) {
                            q.push(neighbor);
                        }
                    }
                }
            }
            if (sort_upd.size() != upd_pg_amt.size()) {
                continue;
            }
            int midIdx=sort_upd.size()/2;
            int midPg=sort_upd[midIdx];
            tot+=midPg;
        }
    }
    cout << tot << endl;
}

int main() {
    part1();
    part2();
}