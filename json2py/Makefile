grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
src=../testbench.json
#src=testbench1.json
#src=testbench5.json
#src=testbench2.json
#src=testbench3.json
#src=helloworld1.json
#src=helloworld2.json
#src=helloworld.json
target=`basename ${src} .json`
here=`pwd`

all:
	${prep} "." '$$' ${grammar} ${format} --stop=1 --fmt=${here}/fmt.js --grammarname=ASC2py <${src} >${target}.py
