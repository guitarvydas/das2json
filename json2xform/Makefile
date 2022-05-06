grammar=../djson.ohm
prep=../prep/prep
format=xdjson.fmt
src=testbench4.json
#src=../testbench.json
target=`basename ${src} .json`
here=`pwd`
gname=ASCxform
support=--fmt=${here}/../json2js/fmt.js

all: main regression

main:
	${prep} "." '$$' ${grammar} ${format} --stop=1 ${support} --grammarname=${gname} <${src} >${target}.js

regression:
	${prep} "." '$$' ${grammar} ${format} --stop=1 ${support} --grammarname=${gname} <${target}.js >${target}-regression.js
	diff ${target}.js ${target}-regression.js

dev: main
	cat ${target}.js
