# convert DPL to JSON
- DPL means "Diagrammatic Programming Language"
- i.e. a programming language whose syntax consists of a hybrid of drawn figures and text
- in this particular case, we use draw.io to create drawings
- the number of different figures is quite small

![Syntax](./syntax.svg)

---

May 5, 2024
write das2json.swib spec (patterned after S/SL) to create a stream-based receptor for the beginnings of a Das2JSON tool
hand-compile das2json.swib to das2json.py
separate das2json.py into 2 .py files - (1) das2json.py and (2) receptor.py
receptor.py contains the code library for building and running receptors, it is the "assembler" for building receptors
das2json.py is the code for walking a .drawio file and to produce identity output, the intention is to get the identity version working, then to hack on it to produce .json from a drawing which contains only semantically useful information

May 7, 2024
SWIB - SoftWare Interlocking Blocks
automate conversion of das2json.swib spec into Python
I use the Transpile component (in a pipeline, twice) to read das2json.swib and to output a valid Python program 
