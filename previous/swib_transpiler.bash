#!/bin/bash
cat py0d.py main.py >_.py
python3 _.py . 0D/python das2json.swib main das2json.drawio.json transpile.drawio.json
