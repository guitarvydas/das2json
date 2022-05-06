

var Phrase_Parser_signature = {
    name: "Phrase_Parser",
    inputs: [{name:"phrase", structure:["phrase"]}],
    outputs: [{name:"order no choices", structure:["order_no_choices"]}, {name:"order with choices", structure:["order_with_choices"]}, {name:"parse error", structure:["parse_error"]}, {name:"hook error", structure:["hook_error"]}]
}


var Phrase_Parser_protoImplementation = {
    name: "Phrase_Parser",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        
    }
}

function Phrase_Parser (container, instancename) {
    let me = new Leaf (Phrase_Parser_signature, Phrase_Parser_protoImplementation, container, instancename);
    return me;
}


