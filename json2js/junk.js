
var Order_Taker_signature = {
    name: "Order_Taker",
    inputs: [{name:"phrase", structure: ["phrase"]}],
    outputs: [{name:"food order", structure: ["food order"]}]
}



function Order_Taker_makechildren (container) {
    var child1 = new Phrase_Parser (container, "Phrase Parser");
    var children = [ child1 ];
    return children;
}

function Order_Taker_makeconnections (container) {
    var conn2 = {sender:{name: "Order Taker", etag: "phrase"}), net: "NIY", receivers: [ [{name: "Phrase Parser", etag: "phrase"})] ]});    
var conn3 = {sender:{name: "Phrase Parser", etag: "order no choices"}), net: "NIY", receivers: [ [{name: "Order Taker", etag: "food order"})] ]});    
var conn4 = {sender:{name: "Phrase Parser", etag: "order with choices"}), net: "NIY", receivers: [ [{name: "Order Taker", etag: "food order"})] ]})
    me.connections = [ conn2, conn3, conn4 ]
}

var Order_Taker_protoImplementation = {
    name: "Order_Taker",
    kind: "container",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        deliverInputMessageToAllChildrenOfSelf (me, message);
    }
}

function Order_Taker (container, instancename) {
    let me = new Container (Order_Taker_signature, Order_Taker_protoImplementation, container, instancename);
    me.children = Order_Taker_makechildren (me);
    me.connections = Order_Taker_makeconnections (me);
    ...
    return me;
}
