
class _HTML_Button (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = []
	self.outputs = ["click"]
        
        self.children = {}
        
	self.connections = [  ]
    def react (self, inputMessage):
        me.send ("click", true);
        return super ().react (inputMessage)

class _Phrase_Faker (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = ["go"]
	self.outputs = ["short phrase", "long phrase"]
        
        self.children = {}
        
	self.connections = [  ]
    def react (self, inputMessage):
        
<div>
</div>
        return super ().react (inputMessage)

class _Phrase_Parser (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = ["phrase"]
	self.outputs = ["order no choices", "order with choices", "parse error", "hook error"]
        
        self.children = {}
        
	self.connections = [  ]
    def react (self, inputMessage):
        
        return super ().react (inputMessage)

class _Test_Bench (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = []
	self.outputs = ["food order"]
        child1 = "HTML Button"._"HTML Button" (dispatcher, self, "HTML Button")
        child2 = "Phrase Faker"._"Phrase Faker" (dispatcher, self, "Phrase Faker")
        child3 = "Order Taker"._"Order Taker" (dispatcher, self, "Order Taker")
        self.children = {"HTML Button":child1, "Phrase Faker":child2, "Order Taker":child3}
        conn4 = mpos.Connector (mpos.Sender ("HTML Button", "click"),  [mpos.Receiver ("Phrase Faker", "go")] })
        conn5 = mpos.Connector (mpos.Sender ("Phrase Faker", "short phrase"),  [mpos.Receiver ("Order Taker", "phrase")] })
        conn6 = mpos.Connector (mpos.Sender ("Phrase Faker", "long phrase"),  [mpos.Receiver ("Order Taker", "phrase")] })
        conn7 = mpos.Connector (mpos.Sender ("Order Taker", "food order"),  [mpos.Receiver ("Test Bench", "food order")] })
	self.connections = [ conn4, conn5, conn6, conn7 ]
    def react (self, inputMessage):
        
        return super ().react (inputMessage)

class _Order_Taker (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
	self.inputs = ["phrase"]
	self.outputs = ["food order"]
        child8 = "Phrase Parser"._"Phrase Parser" (dispatcher, self, "Phrase Parser")
        self.children = {"Phrase Parser":child8}
        conn9 = mpos.Connector (mpos.Sender ("Order Taker", "phrase"),  [mpos.Receiver ("Phrase Parser", "phrase")] })
        conn10 = mpos.Connector (mpos.Sender ("Phrase Parser", "order no choices"),  [mpos.Receiver ("Order Taker", "food order")] })
        conn11 = mpos.Connector (mpos.Sender ("Phrase Parser", "order with choices"),  [mpos.Receiver ("Order Taker", "food order")] })
	self.connections = [ conn9, conn10, conn11 ]
    def react (self, inputMessage):
        
        return super ().react (inputMessage)

