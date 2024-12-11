#!/bin/bash
set -e
D2J=./das2json-bootstrap/mac/das2json
${D2J} sp2py.drawio
./gen-py.bash das2json.sp generated.py

echo '*** Javascript not generated ***' >generated.mjs
