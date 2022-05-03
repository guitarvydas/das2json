grammar=../djson.ohm
prep=../prep/prep
format=djson.fmt
src=../testbench.json
here=`pwd`
begin='.'
end='$'

all:
	${prep} "${begin}" "${end}" ${grammar} ${format} --stop=1 --support=${here}/support.js <${src}
