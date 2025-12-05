#include <iostream>
#include <regex>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::istreambuf_iterator;
using std::regex;
using std::sregex_iterator;
using std::stoi;
using std::string;

int main() {
    long long part1 = 0;
    long long part2 = 0;
    bool enabled = true;
    regex pattern(R"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))");

    string text((istreambuf_iterator<char>(cin)),
                istreambuf_iterator<char>());

    sregex_iterator it(text.begin(), text.end(), pattern);
    sregex_iterator it_end;

    for(; it != it_end; ++it) {
        auto match = *it;

        if(match[0].length() == 4) {
            enabled = false;
        } else if(match[0].length() == 7) {
            enabled = true;
        } else {
            int value = stoi(match[1].str()) * stoi(match[2].str());
            part1 += value;
            part2 += value * enabled;
        }
    }

    cout << part1 << endl;
    cout << part2 << endl;

    return 0;
}
