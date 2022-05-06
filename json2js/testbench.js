

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
            me.send ("long phrase", "I Want A Hamburger With Ketchup And Bacon And Pickles");



    }
}

function Phrase_Faker (container, instancename) {
    let me = new Leaf (Phrase_Faker_signature, Phrase_Faker_protoImplementation, container, instancename);
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



var Test_Bench_signature = {
    name: "Test_Bench",
    inputs: [],
    outputs: [{name:"food order", structure:["food_order"]}]
}



function Test_Bench_makechildren (container) {
      var child1 = new HTML_Button (container, "HTML Button");
        var child2 = new Phrase_Faker (container, "Phrase Faker");
        var child3 = new Order_Taker (container, "Order Taker");
      var children = [ {name: "HTML Button", runnable: child1}, {name: "Phrase Faker", runnable: child2}, {name: "Order Taker", runnable: child3} ];
      return children;
}

function Test_Bench_makeconnections (container) {
    var conn4 = {sender:{name: "HTML Button", etag: "click"}, net: "NIY", receivers:  [{name: "Phrase Faker", etag: "go"}] };
    var conn5 = {sender:{name: "Phrase Faker", etag: "short phrase"}, net: "NIY", receivers:  [{name: "Order Taker", etag: "phrase"}] };
    var conn6 = {sender:{name: "Phrase Faker", etag: "long phrase"}, net: "NIY", receivers:  [{name: "Order Taker", etag: "phrase"}] };
    var conn7 = {sender:{name: "Order Taker", etag: "food order"}, net: "NIY", receivers:  [{name: "_me", etag: "food order"}] };
    var connections = [ conn4, conn5, conn6, conn7 ];
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



var Order_Taker_signature = {
    name: "Order_Taker",
    inputs: [{name:"phrase", structure:["phrase"]}],
    outputs: [{name:"food order", structure:["food_order"]}]
}



function Order_Taker_makechildren (container) {
      var child8 = new Phrase_Parser (container, "Phrase Parser");
      var children = [ {name: "Phrase Parser", runnable: child8} ];
      return children;
}

function Order_Taker_makeconnections (container) {
    var conn9 = {sender:{name: "_me", etag: "phrase"}, net: "NIY", receivers:  [{name: "Phrase Parser", etag: "phrase"}] };
    var conn10 = {sender:{name: "Phrase Parser", etag: "order no choices"}, net: "NIY", receivers:  [{name: "_me", etag: "food order"}] };
    var conn11 = {sender:{name: "Phrase Parser", etag: "order with choices"}, net: "NIY", receivers:  [{name: "_me", etag: "food order"}] };
    var connections = [ conn9, conn10, conn11 ];
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


