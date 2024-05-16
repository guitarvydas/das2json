convert_drawing_to_json: das2json.py
	./convert_drawing_to_json.bash

das2json.py:
	./transpile_swib_to_python.bash

clean:
	rm -rf *.json das2json.py
	rm -rf *~


#########

# to install required libs, once
install-js-requires:
	npm install yargs prompt-sync

