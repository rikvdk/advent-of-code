#!/bin/bash

year=${AOC_YEAR:-$(date +%Y)}
day=${AOC_DAY:-$(date +%d)}
lang=${AOC_LANG:-py}

mkdir -p ./$year/$day
cp -r ./templates/$lang ./$year/$day

if [ $AOC_SESSION ]; then
    curl -s "https://adventofcode.com/$year/day/$(expr $day + 0)/input" --cookie "session=$AOC_SESSION" --output ./$year/$day/input
fi
