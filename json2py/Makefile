grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
src=../testbench.json
here=`pwd`

all:

	${prep} "." '$$' ${grammar} ${format} --stop=1 --support=${here}/support.js --grammarname=ASC2py <${src}
