grammar=../djson.ohm
prep=../prep/prep
format=identity-djson.fmt
#src=testbench4.json
src=../testbench.json
target=`basename ${src} .json`
here=`pwd`

all: main regression

main:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASCconnection <${src} >${target}.js

regression:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASCconnection <${target}.js >${target}-regression.js
	diff ${target}.js ${target}-regression.js

dev: main
	cat ${target}.js
