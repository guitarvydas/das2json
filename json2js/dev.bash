#!/bin/bash

grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
src=../testbench.json
here=`pwd`
begin='.'
end='$'

${prep} "${begin}" "${end}" ${grammar} ${format} --stop=1 --support=${here}/support.js <${src}
