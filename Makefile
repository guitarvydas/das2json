all:
	@echo 'ensure that formatted text option in draw.io is disabled everywhere'
	./0d/das2json/das2json das2json-swib.drawio
	python3 main.py . 0D/python test.txt main das2json-swib.drawio.json


hold:
	./all.bash

convert_drawing_to_json: das2json.py
	./convert_drawing_to_json.bash

das2json.py: py0d.bash
	./transpile_swib_to_python.bash

py0d.bash :
	./make_py0d.bash

clean:
	rm -rf *.json das2json.py
	rm -rf *~


#########

# to install required libs, once
install-js-requires:
	npm install yargs prompt-sync

