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
    auto part1 = 0LL;
    auto part2 = 0LL;
    auto enabled = true;

    auto text = string((istreambuf_iterator<char>(cin)),
                       istreambuf_iterator<char>());

    auto pattern = regex(R"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))");
    auto it = sregex_iterator(text.cbegin(), text.cend(), pattern);
    auto it_end = sregex_iterator();

    for(; it != it_end; ++it) {
        auto match = *it;

        if(match[0].length() == 4) {
            enabled = false;
        } else if(match[0].length() == 7) {
            enabled = true;
        } else {
            auto value = stoi(match[1].str()) * stoi(match[2].str());
            part1 += value;
            part2 += value * enabled;
        }
    }

    cout << part1 << endl;
    cout << part2 << endl;

    return 0;
}
