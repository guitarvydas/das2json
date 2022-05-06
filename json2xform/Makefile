grammar=../djson.ohm
prep=../prep/prep
format=identity-djson.fmt
#src=testbench4.json
src=../testbench.json
target=`basename ${src} .json`
here=`pwd`
gname=ASCxform

all: main regression

main:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=${gname} <${src} >${target}.js

regression:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=${gname} <${target}.js >${target}-regression.js
	diff ${target}.js ${target}-regression.js

dev: main
	cat ${target}.js
