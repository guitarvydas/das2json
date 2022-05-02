NODEMODULES=\
	~/node_modules/ohm-js \
	~/node_modules/yargs \
	~/node_modules/atob \
	~/node_modules/pako

# change this for your own environment
TOOLS=.

all: case4.json
#all: testbench.json

main_all: $(NODEMODULES) tools topbuildscript.py
	./topbuildscript.py

bootstrap : $(NODEMODULES) tools bootstrap_helloworld.json topbuildscript.py

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

testbench.json : tools testbench.drawio
	./generate.bash $(TOOLS) testbench.drawio
	mv out.json testbench.json

case4.json : tools case4.drawio
	./generate.bash $(TOOLS) case4.drawio
	mv out.json case4.json

case0.json : tools case0.drawio
	./generate.bash $(TOOLS) case0.drawio
	mv out.json case0.json
case1.json : tools case1.drawio
	./generate.bash $(TOOLS) case1.drawio
	mv out.json case1.json
case2.json : tools case2.drawio
	./generate.bash $(TOOLS) case2.drawio
	mv out.json case2.json
case3.json : tools case3.drawio
	./generate.bash $(TOOLS) case3.drawio
	mv out.json case3.json

bootstrap_helloworld.json : tools helloworld.drawio
	./generate.bash $(TOOLS) helloworld.drawio
	mv out.json helloworld.json

# helloworld.py : helloworld.json
# 	./transpile2py.bash helloworld.drawio helloworld.json
# 	chmod a+x top.py
# 	./top.py

buildscript.json : tools buildscript.drawio
	./generate.bash $(TOOLS) buildscript.drawio
	mv out.json buildscript.json

topbuildscript.py : buildscript.json transpile2py.bash pyemit.py
	./transpile2py.bash buildscript.drawio buildscript.json
	mv top.py topbuildscript.py
	chmod a+x topbuildscript.py

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

