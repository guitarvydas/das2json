

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



var HTML_Buttonza_signature = {
    name: "HTML_Buttonza",
    inputs: [],
    outputs: [{name:"clicka", structure:["clicka"]}]
}


var HTML_Buttonza_protoImplementation = {
    name: "HTML_Buttonza",
    kind: "leaf",
    begin: function () {},
    finish: function () {},
    handler: function (me, message) {
        me.senda ("click", true);
    }
}

function HTML_Buttonza (container, instancename) {
    let me = new Leaf (HTML_Buttonza_signature, HTML_Buttonza_protoImplementation, container, instancename);
    return me;
}


