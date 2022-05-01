import mpos

class Dispatcher:
    # the Dispatcher deals with Component instances, but everything else (e.g. Messages) uses string ids
    registry = []  # in this examples, registry is a flat list actual part instances (not names)
    outputBucket = None

    def register (self, instance):
        self.registry.append (instance)

    def dispatch (self):
        # dispatch is a loop within a loop, we break out the inner loop as a function dispatch1 for this example
        while self.anyComponentReadyP ():
            self.dispatch1 ()

    def dispatch1 (self):
        for instance in self.registry:
            if instance.readyP ():
                message = instance.popFirstInput ()
                outputs = self.invokeComponent (instance, message)
                self.dumpOutputBucket (instance, outputs)
                 


    def anyComponentReadyP (self):
        for instance in self.registry:
            if instance.readyP ():
                return True
        return False

    def invokeComponent (self, instance, message):
        instance.clearOutputBucket ()
        assert (instance.idInParent == message.component), "internal error - message.component.id should be the same as the instance.idInParent"
        return instance.react (message)

    def dumpOutputBucket (self, instance, outputBucket):
        if instance:
         if instance.hasOutputsP ():
                container = instance.getContainer ()
                for outputMessage in outputBucket:
                    connection = container.findConnectionBasedOnMessage (outputMessage) # <<< search is based on instance id within Container
                    receiversList = connection.getReceivers ()
                    for receiver in receiversList:
                        instance = container.mapNameToInstance (receiver.component)
                        inputMessage = self.mapOutputMessageToInputMessage (outputMessage, receiver)
                        instance.enqueueInput (inputMessage)
        else:
            for m in outputBucket:
                print (m) # top level has no container, just dump message to stdout


    def mapOutputMessageToInputMessage (self, outputMessage, receiver):
        m = mpos.InputMessage (receiver.component, receiver.tag, outputMessage.data)
        return m

