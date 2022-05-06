grammar=../djson.ohm
prep=../prep/prep
format=xdjson.fmt
identity=identity-djson.fmt
#src=testbench4.json
src=testbench6.json
#src=../testbench.json
target=`basename ${src} .json`
here=`pwd`
gname=ASCxform
support=--fmt=${here}/../json2js/fmt.js
reformat=xdjson2.fmt

all: main regression

main:
	${prep} "." '$$' ${grammar} ${format} --stop=1 ${support} --grammarname=${gname} <${src} >${target}.js

identity:
	${prep} "." '$$' ${grammar} ${identity} --stop=1 ${support} --grammarname=${gname} <${src} >${target}-identity.js

regression:
	${prep} "." '$$' ${grammar} ${format} --stop=1 ${support} --grammarname=${gname} <${target}.js >${target}-regression.js
	diff ${target}.js ${target}-regression.js

dev: identity
	${prep} "." '$$' ${grammar} ${format} --stop=1 ${support} --grammarname=${gname} <${src} >${target}-1.js
	${prep} "." '$$' ${grammar} ${reformat} --stop=1 ${support} --grammarname=${gname} <${target}-1.js >${target}-2.js
	cat ${target}-2.js
	diff ${target}-identity.js ${target}-2.js
