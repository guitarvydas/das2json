#!/bin/bash
# run das2json.py to convert test.drawio into a .json file containing only semantic info
#echo 'if strange errors occur, then, grep "arrow has no target" das2json.py'
python3 das2json.py <test.drawio # das2json.py parses test.drawio and emits .json to stdout
