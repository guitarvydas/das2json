grammar=../djson.ohm
prep=../prep/prep
format=identity-djson.fmt
src=testbench4.json
#src=../testbench.json
target=`basename ${src} .json`
here=`pwd`

all:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASCconnection <${src} >${target}.js
	cat ${target}.js
