

var Phrase_Faker_signature = {
    name: "Phrase_Faker",
    inputs: [{name:"go", structure: ["go"]}],
    outputs: [{name:"short phrase", "long phrase", structure: ["short phrase", "long phrase"]}]
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


