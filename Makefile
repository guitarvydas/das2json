NODEMODULES=\
	~/node_modules/ohm-js \
	~/node_modules/yargs \
	~/node_modules/atob \
	~/node_modules/pako

# change this for your own environment
TOOLS=.

all: $(NODEMODULES) tools helloworld.json topd2py.py

~/node_modules/ohm-js:
	npm install ohm-js
~/node_modules/yargs:
	npm install yargs
~/node_modules/atob:
	npm install atob
~/node_modules/pako:
	npm install pako

tools:
	(cd ./dr ; make)
	(cd ./prep ; make)
	(cd ./d2f ; make)
	(cd ./das2f ; make)
	(cd ./das2j ; make)

helloworld.json : tools helloworld.drawio
	./generate.bash $(TOOLS) helloworld.drawio
	mv out.json helloworld.json

# helloworld.py : helloworld.json
# 	./transpile2py.bash helloworld.drawio helloworld.json
# 	chmod a+x top.py
# 	./top.py

d2py.json : tools d2py.drawio
	./generate.bash $(TOOLS) d2py.drawio
	mv out.json d2py.json

topd2py.py : d2py.json transpile2py.bash pyemit.py
	./transpile2py.bash d2py.drawio d2py.json
	mv top.py topd2py.py
	chmod a+x topd2py.py
	./topd2py.py

clean:
	(cd ./dr ; make clean)
	(cd ./prep ; make clean)
	(cd ./d2f ; make clean)
	(cd ./das2f ; make clean)
	(cd ./das2j ; make clean)
	rm -f layer*
	rm -f preprocessed*
	rm -f duct?_*
	rm -f *.json
	rm -rf _*
	rm -f *~

