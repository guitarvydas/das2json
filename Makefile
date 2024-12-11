all:
	@echo 'ensure that formatted text option in draw.io is disabled everywhere'
	python3 choreographer.py

clean:
	rm -rf *.json das2json.py
	rm -rf *~


#########

# to install required libs, once
install-js-requires:
	npm install yargs prompt-sync

# python3 -m venv ./sp
# source sp/bin/activate #activate "sp" Python environment
# pip3 install websockets
