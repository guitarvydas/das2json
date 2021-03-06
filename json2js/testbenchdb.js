

var probe1_signature = {
    name: "probe1",
    inputs: [{name:"in", structure:["in"]}],
    outputs: [{name:"out", structure:["out"]}]
}


var probe1_protoImplementation = {
    name: "probe1",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('probe 1: ');
console.log (message);
me.send ("out", message.data);
    }
}

function probe1 (container, instancename) {
    let me = new Leaf (probe1_signature, probe1_protoImplementation, container, instancename);
    return me;
}



var Phrase_Faker_signature = {
    name: "Phrase_Faker",
    inputs: [{name:"go", structure:["go"]}],
    outputs: [{name:"short phrase", structure:["short_phrase"]}, {name:"long phrase", structure:["long_phrase"]}]
}


var Phrase_Faker_protoImplementation = {
    name: "Phrase_Faker",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('phrase faker: ' + message.etag);    me.send ("long phrase", "I Want A Hamburger With Ketchup And Cheese And Pickles");



    }
}

function Phrase_Faker (container, instancename) {
    let me = new Leaf (Phrase_Faker_signature, Phrase_Faker_protoImplementation, container, instancename);
    return me;
}



var probe2_signature = {
    name: "probe2",
    inputs: [{name:"in", structure:["in"]}],
    outputs: [{name:"out", structure:["out"]}]
}


var probe2_protoImplementation = {
    name: "probe2",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('probe 2: ');
console.log (message);
me.send ("out", message.data);
    }
}

function probe2 (container, instancename) {
    let me = new Leaf (probe2_signature, probe2_protoImplementation, container, instancename);
    return me;
}



var Order_Taker_signature = {
    name: "Order_Taker",
    inputs: [{name:"phrase", structure:["phrase"]}],
    outputs: [{name:"food order", structure:["food_order"]}]
}



function Order_Taker_makechildren (container) {
      var child1 = new Phrase_Parser (container, "Phrase Parser");
        var child2 = new probe3 (container, "probe3");
        var child3 = new probe3a (container, "probe3a");
      var children = [ {name: "Phrase Parser", runnable: child1}, {name: "probe3", runnable: child2}, {name: "probe3a", runnable: child3} ];
      return children;
}

function Order_Taker_makeconnections (container) {
    var conn4 = {sender:{name: "_me", etag: "phrase"}, net: "NIY", receivers:  [{name: "probe3", etag: "in"}] };
    var conn5 = {sender:{name: "Phrase Parser", etag: "order with choices"}, net: "NIY", receivers:  [{name: "probe3a", etag: "in"}] };
    var conn6 = {sender:{name: "probe3", etag: "out"}, net: "NIY", receivers:  [{name: "Phrase Parser", etag: "phrase"}] };
    var conn7 = {sender:{name: "probe3a", etag: "out"}, net: "NIY", receivers:  [{name: "_me", etag: "food order"}] };
    var connections = [ conn4, conn5, conn6, conn7 ];
    return connections;
}

function Order_Taker_makenets (container) {
    return [];
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
    me.nets =  Order_Taker_makenets (me);
    me.deliver_input_from_container_input_to_child_input = deliver_input_from_container_input_to_child_input;
    me.deliver_input_from_container_input_to_me_output = deliver_input_from_container_input_to_me_output;
    return me;
}



var Phrase_Parser_signature = {
    name: "Phrase_Parser",
    inputs: [{name:"phrase", structure:["phrase"]}],
    outputs: [{name:"order no choices", structure:["order_no_choices"]}, {name:"order with choices", structure:["order_with_choices"]}, {name:"parse error", structure:["parse_error"]}, {name:"hook error", structure:["hook_error"]}]
}



function Phrase_Parser (container, instancename) {
    let me = new Leaf (Phrase_Parser_signature, Phrase_Parser_protoImplementation, container, instancename);
    return me;
}



var probe3_signature = {
    name: "probe3",
    inputs: [{name:"in", structure:["in"]}],
    outputs: [{name:"out", structure:["out"]}]
}


var probe3_protoImplementation = {
    name: "probe3",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('probe 3:');
console.log (message);
me.send ("out", message.data);
    }
}

function probe3 (container, instancename) {
    let me = new Leaf (probe3_signature, probe3_protoImplementation, container, instancename);
    return me;
}



var probe4_signature = {
    name: "probe4",
    inputs: [{name:"in", structure:["in"]}],
    outputs: [{name:"out", structure:["out"]}]
}


var probe4_protoImplementation = {
    name: "probe4",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('probe 4 (woohoo): '); console.log (message);
me.send ("out", message.data);
    }
}

function probe4 (container, instancename) {
    let me = new Leaf (probe4_signature, probe4_protoImplementation, container, instancename);
    return me;
}



var probe3a_signature = {
    name: "probe3a",
    inputs: [{name:"in", structure:["in"]}],
    outputs: [{name:"out", structure:["out"]}]
}


var probe3a_protoImplementation = {
    name: "probe3a",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        console.log ('probe 3a:');
console.log (message);
me.send ("out", message.data);
    }
}

function probe3a (container, instancename) {
    let me = new Leaf (probe3a_signature, probe3a_protoImplementation, container, instancename);
    return me;
}



var Test_Bench_signature = {
    name: "Test_Bench",
    inputs: [],
    outputs: [{name:"food order", structure:["food_order"]}]
}



function Test_Bench_makechildren (container) {
      var child8 = new probe1 (container, "probe1");
        var child9 = new Phrase_Faker (container, "Phrase Faker");
        var child10 = new probe2 (container, "probe2");
        var child11 = new Order_Taker (container, "Order Taker");
        var child12 = new probe4 (container, "probe4");
        var child13 = new HTML_Button (container, "HTML Button");
      var children = [ {name: "probe1", runnable: child8}, {name: "Phrase Faker", runnable: child9}, {name: "probe2", runnable: child10}, {name: "Order Taker", runnable: child11}, {name: "probe4", runnable: child12}, {name: "HTML Button", runnable: child13} ];
      return children;
}

function Test_Bench_makeconnections (container) {
    var conn14 = {sender:{name: "probe1", etag: "out"}, net: "NIY", receivers:  [{name: "Phrase Faker", etag: "go"}] };
    var conn15 = {sender:{name: "Phrase Faker", etag: "long phrase"}, net: "NIY", receivers:  [{name: "probe2", etag: "in"}] };
    var conn16 = {sender:{name: "probe2", etag: "out"}, net: "NIY", receivers:  [{name: "Order Taker", etag: "phrase"}] };
    var conn17 = {sender:{name: "Order Taker", etag: "food order"}, net: "NIY", receivers:  [{name: "probe4", etag: "in"}] };
    var conn18 = {sender:{name: "probe4", etag: "out"}, net: "NIY", receivers:  [{name: "_me", etag: "food order"}] };
    var conn19 = {sender:{name: "HTML Button", etag: "click"}, net: "NIY", receivers:  [{name: "probe1", etag: "in"}] };
    var connections = [ conn14, conn15, conn16, conn17, conn18, conn19 ];
    return connections;
}

function Test_Bench_makenets (container) {
    return [];
}

var Test_Bench_protoImplementation = {
    name: "Test_Bench",
    kind: "container",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        deliverInputMessageToAllChildrenOfSelf (me, message);
    }
}

function Test_Bench (container, instancename) {
    let me = new Container (Test_Bench_signature, Test_Bench_protoImplementation, container, instancename);
    me.children = Test_Bench_makechildren (me);
    me.connections = Test_Bench_makeconnections (me);
    me.nets =  Test_Bench_makenets (me);
    me.deliver_input_from_container_input_to_child_input = deliver_input_from_container_input_to_child_input;
    me.deliver_input_from_container_input_to_me_output = deliver_input_from_container_input_to_me_output;
    return me;
}



var HTML_Button_signature = {
    name: "HTML_Button",
    inputs: [],
    outputs: [{name:"click", structure:["click"]}]
}


var HTML_Button_protoImplementation = {
    name: "HTML_Button",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        me.send ("click", true);
    }
}

function HTML_Button (container, instancename) {
    let me = new Leaf (HTML_Button_signature, HTML_Button_protoImplementation, container, instancename);
    return me;
}


