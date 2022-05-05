

var Order_Taker_signature = {
    name: "Order_Taker",
    inputs: [{name:"phrase", structure: ["phrase"]}],
    outputs: [{name:"food order", structure: ["food order"]}]
}



function Order_Taker_makechildren (me) {
      var child1 = new Phrase_Parser (me, "Phrase Parser");
}

var Order_Taker_protoImplementation = {
    name: "Order_Taker",
    kind: "container",
    begin: function () {},
    finish: function () {},
    self.connections = [ conn2, conn3, conn4 ]
    handler: function (me, message) {
        deliverInputMessageToAllChildrenOfSelf (me, message);
    }
}

function Order_Taker (container, instancename) {
    let me = new Container (Order_Taker_signature, Order_Taker_protoImplementation, container, instancename);
    me.children = Order_Taker_makechildren (me);
    ...
    return me;
}


