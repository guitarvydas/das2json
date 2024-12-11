#!/bin/bash
# usage ./generate-chunk.bash ${SRC} xxx-generated.py
echo generate chunk py $1 $2
set -e
src=$1
gen=$2
cat kernel.py main.py >_.py
python3 _.py . . ${src} main sp2py.drawio.json >${gen}
python3 mvline.py  ${gen} 60 >/tmp/${gen}
mv /tmp/${gen} ./${gen}
python3 errcheck.py ${gen}
