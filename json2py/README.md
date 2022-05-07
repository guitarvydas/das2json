Unfinished

convert diagram to JSON
convert JSON to Python

usage: make

see also ../das, esp. helloworld.drawio -> helloworld.json

2 steps:
1. convert testbench.drawio -> testbench.json
2. convert testbench.json -> testbench.py

Step 1 is done in ../
Step 2 uses the Makefile.

Step 2 uses prep, which uses Ohm-JS and `../djson.ohm` and `./djson.fmt`.

`djson.fmt` is a formatter which groks Components described as JSON, then outputs a Python program.

WIP:

- using ../das/helloworld.py as a test case to see if the output matches hand-written output from ../das/{hello.py, world.py, helloworld.py}

- next up: rewrite `djson.fmt` for JS in ../json2js

