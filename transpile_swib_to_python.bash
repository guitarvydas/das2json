#!/bin/bash
# builds das2json.py from diagram (das2json.drawio)
# diagram -> das2json.py uses bootstrapping py0D
0D/das2json/das2json 0D/python/std/transpile.drawio
0D/das2json/das2json das2json.drawio
python3 py0d.py . 0D/python das2json.swib main das2json.drawio.json transpile.drawio.json >das2json.py
