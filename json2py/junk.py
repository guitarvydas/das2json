../prep/prep "." '$' ../djson.ohm djson.fmt --stop=1 --fmt=`pwd`/fmt.js --grammarname=ASC2py <helloworld1.json

class _hello (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = ["a"]
	self.outputs = ["out"]
        
        self.children = {}
    def react (self, inputMessage):
        self.send ("out", True)


        return super ().react (inputMessage)

