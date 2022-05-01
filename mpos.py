import sys
import dispatcher
import queue

from typing import NoReturn

# for now, component is a name (string) local to Container

class Sender:
    def __init__ (self, c,p):
        self.component = c
        self.tag = p

    def __eq__ (self, other):
        if isinstance(other, Sender):
            return self.component == other.component and self.tag == other.tag
        else:
            return False

    def asSender (self):
        return self

class Receiver:
    def __init__ (self, c, p):
        self.component = c
        self.tag = p

    def deliverOutputMessageToInputTagOfReceiver (self, outputMessage):
        inputMessage = InputMessage (self.component, self.tag, outputMessage.data)
        component = self.component
        component.enqueueInput (inputMessage)

class MessageCommon: # this class should not be instantiated directly (use InputMessage or OutputMessage)
    # a message is identified by {component X tag}
    # .component is "" for "self"
    # an OutputMessage has (normally) a different "component" and "tag" than an InputMessage
    # OutputMessage is relative to the Sender
    # InputMessage is relative to the Receiver
    # an OutputMessage is created by Send ()
    # an InputMessage is (normally) created by the Dispatcher during dumping of the output bucket of a Component after it has performed a reaction
    # the mapping from OutputMessage to InputMessage is defined in the Connections of the parent Container
    # [Connections is a routing table contained in the parent Container]
    # a container can:
    #  (1) route messages between its children, 
    #  (2) route its input to its children, 
    #  (3) route a child's output to its own output, 
    #  (4) route its own input to its own output
    #  (5) route a child's output to NOWHERE (N/C - no connection)
    #  (6) route its own input to NOWHERE (N/C)
    # IOW - a message is { id, data } where id is { component X tag }
    # the fact that "component" is always included in the id ensures that the message has relative addressing (relative to Sender or Receiver as appropriate)
    # Aside: "tag" is called "pin" in electronics, "tag" is called "topic" in pubsb (e.g. ROS)
    # Aside: N/C has no parallel in Functional notation, Natural Numbers vs. Whole Numbers (Naturals do not contain 0, Whole Numbers contain 0)

    def __init__ (self, c, p, d):
        self.component = c
        self.tag = p
        self.data = d

    def sender (self):
        s = Sender (self.component, self.tag)
        return s

    def getTag (self):
        return self.tag
    
    def getComponent (self):
        return self.component

class InputMessage (MessageCommon):
    pass

class OutputMessage (MessageCommon):
    pass

class MessageFifo (queue.Queue):
    def enqueue (self, m):
        self.put (m)

    def dequeue (self):
        return self.get ()

    def emptyP (self):
        return self.empty ()

class Connector:
    def __init__ (self, senders, receivers):
        self.senders = senders
        self.receivers = receivers
    
    def getReceivers (self):
        return self.receivers

    def containsSenderP (self, sender):
        for s in self.senders:
            if (s == sender):
                return True
        return False
    
class Component:
        def __init__ (self, dispatcher, container, id):
            self.inputs = []
            self.outputs = []
            self.outputBucket = []
            self.parent = container
            self.idInParent = id
            self.inputQueue = MessageFifo ()
            self.reaction = None
            dispatcher.register (self)

        def popFirstInput (self):
            if self.inputQueue.emptyP ():
                return None
            else:
                message = self.inputQueue.dequeue ()
                return message
        
        def clearOutputBucket (self):
            self.outputBucket = []

        def readyP (self):
            return 0 < self.inputQueue._qsize ()

        def enqueueInput (self, m):
            self.inputQueue.enqueue (m)

        def kickstart (self):
            m = InputMessage (self.idInParent, "go", True)
            self.enqueueInput (m)

        def send (self, tag, data):
            message = OutputMessage (self.idInParent, tag, data)
            self.outputBucket.append (message)

        def react (self, message):
            return self.outputBucket

        def getContainer (self):
            return self.parent

        def hasOutputsP (self):
            return (0 < len (self.outputBucket))


        def panic (self, message):
            print ("\n*****")
            print (message, file=sys.stderr)
            print ("*****\n")
            sys.exit (1)
            
        def quit (self, message):
            self.panic (message)

class Leaf (Component):
    pass

class Container (Component):
    def __init__ (self, dispatcher, parent, debugID):
        super ().__init__ (dispatcher, parent, debugID)
        self.children = []
        self.connections = []

    def busyP (self):
        for child in self.children:
            if child.busyP ():
                return True
        return False

    def propagateInputToChildren (self, m):
        conn = self.findConnectionBasedOnMessage (m)
        receivers = conn.getReceivers ()
        for r in receivers:
            msg = InputMessage (r.component, r.tag, m.data)
            instance = self.mapNameToInstance (r.component)
            instance.enqueueInput (msg)
        
    def findConnectionBasedOnMessage (self, m):
        for conn in self.connections:
            if (conn.containsSenderP (m.sender ())):
                return conn
        self.panic (f"MPOS: internal error in findConnectionBasedOnMessage tag={m.getTag ()}")

    def mapNameToInstance (self, localName):
        if (localName == ''):
            return self
        else:
            mapped = self.findNameInChildrenMap (localName)
            if mapped:
                return mapped
            else:
                assert "internal error 21"

    def findNameInChildrenMap (self, name):
        return self.children [name]

    def react (self, message):
        self.propagateInputToChildren (message)
        return super ().react (message)

    
