_00_=.
_0D_=0D/python
das2jsondir=./0D/das2json
_STD_ = ${_0D_}/std

0D = ${_0D_}/gensym.py \
    ${_0D_}/datum.py \
    ${_0D_}/message.py \
    ${_0D_}/dynrouting.py \
    ${_0D_}/container.py \
    ${_0D_}/registry.py \
    ${_0D_}/process.py \
    ${_0D_}/0d.py \
    ${_STD_}/std.py \
    ${_STD_}/lib.py \
    ${_STD_}/fakepipe.py \
    ${_STD_}/transpiler.py \
    ${_STD_}/stock.py \
    ${_STD_}/run.py

D2J=${das2jsondir}/das2json
SRC=das2json.swib


#########

# run das2json.py to convert test.drawio into a .json file containing only semantic info
run: das2json.py
	./clr
	@echo 'if strange errors occur, then, grep "arrow has no target" das2json.py'
	python3 das2json.py <test.drawio >temp.json # das2json.py parses test.drawio and emits .json to stdout
	@./cleanup.bash temp.json


#########

# builds das2json.py from diagram (das2json.drawio)
das2json.py:
	make -s compileswib >das2json.py


# diagram -> das2json.py uses bootstrapping py0D
compileswib: py0d.py das2json.drawio.json transpile.drawio.json
	python3 py0d.py ${_00_} ${_0D_} ${SRC} main das2json.drawio.json transpile.drawio.json

py0d.py : main.py ${0D}
	cat ${0D} main.py >py0d.py

das2json.drawio.json: das2json.drawio
	$(D2J) das2json.drawio

transpile.drawio.json: $(_STD_)/transpile.drawio
	$(D2J) $(_STD_)/transpile.drawio

### end build das2json.py

#########

clean:
	rm -rf *.json das2json.py
	rm -rf *~


#########

# to install required libs, once
install-js-requires:
	npm install yargs prompt-sync

