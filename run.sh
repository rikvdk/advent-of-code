#!/bin/bash

year=${AOC_YEAR:-$(date +%Y)}
day=${AOC_DAY:-$(date +%d)}
lang=${AOC_LANG:-py}

if [ $lang = "py" ]; then
    python3 ./$year/$day/py/main.py < ./$year/$day/input
else
    echo "unrecognized language '$lang'"
fi

