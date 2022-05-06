

var Test_Bench_3_signature = {
    name: "Test_Bench_3",
    inputs: [],
    outputs: [{name:"food order", structure:["food_order"]}]
}



function Test_Bench_3_makechildren (container) {
      var child1 = new HTML_Button (container, "HTML Button");
        var child2 = new Phrase_Faker (container, "Phrase Faker");
        var child3 = new Order_Taker (container, "Order Taker");
      var children = [ {name: "HTML Button", runnable: child1}, {name: "Phrase Faker", runnable: child2}, {name: "Order Taker", runnable: child3} ];
      return children;
}

function Test_Bench_3_makeconnections (container) {
    var conn4 = {sender:{name: "HTML Button", etag: "click"}, net: "NIY", receivers:  [{name: "Phrase Faker", etag: "go"}] };
    var connections = [ conn4 ];
    return connections;
}

function Test_Bench_3_makenets (container) {
    return [];
}

var Test_Bench_3_protoImplementation = {
    name: "Test_Bench_3",
    kind: "container",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        deliverInputMessageToAllChildrenOfSelf (me, message);
    }
}

function Test_Bench_3 (container, instancename) {
    let me = new Container (Test_Bench_3_signature, Test_Bench_3_protoImplementation, container, instancename);
    me.children = Test_Bench_3_makechildren (me);
    me.connections = Test_Bench_3_makeconnections (me);
    me.nets =  Test_Bench_3_makenets (me);
    me.deliver_input_from_container_input_to_child_input = deliver_input_from_container_input_to_child_input;
    me.deliver_input_from_container_input_to_me_output = deliver_input_from_container_input_to_me_output;
    return me;
}


