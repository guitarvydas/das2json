grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
#src=testbench1.json
#src=testbench5.json
#src=testbench2.json
#src=testbench3.json
#src=testbench4.json
#src=testbench6.json
#src=../testbenchdb.json
src=../testbench.json
target=`basename ${src} .json`
here=`pwd`

xg=ASCxform
xfmt1=../json2xform/xdjson.fmt
xfmt2=../json2xform/xdjson2.fmt

dev:
	(cd .. ; make ${target}.json)
	cp ../${target}.json .
	${prep} "." '$$' ${grammar} ${xfmt1} --stop=1 --fmt=${here}/fmt.js --grammarname=${xg} <${src} >${target}-1.json
	${prep} "." '$$' ${grammar} ${xfmt2} --stop=1 --fmt=${here}/fmt.js --grammarname=${xg} <${target}-1.json >${target}-2.json
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASC2py --errorview <${target}-2.json >${target}.js
#  	cat ${target}.js

