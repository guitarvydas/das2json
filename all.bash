#!/bin/bash
# run all steps without make
set -e
set -x
./make_py0d.bash
./transpile_swib_to_python.bash
./convert_drawing_to_json.bash
