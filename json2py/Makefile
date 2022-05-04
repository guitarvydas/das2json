grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
#src=../testbench.json
src=testbench1.json
here=`pwd`

all:

	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASC2py <${src}
