let parameters = {};
function pushParameter (name, v) {
    if (!parameters [name]) {
	parameters [name] = [];
    }
    parameters [name].push (v);
}
function popParameter (name) {
    parameters [name].pop ();
}
function getParameter (name) {
    return parameters [name];
}


let _rewrite = {

text : function (c,) {
enter_rule ("text");
    set_return (`${c.rwr ().join ('')}`);
return exit_rule ("text");
},
char_nl : function (s,) {
enter_rule ("char_nl");
    set_return (`⎩${getlineinc ()}⎭\n`);
return exit_rule ("char_nl");
},
char_string : function (lq,cs,rq,) {
enter_rule ("char_string");
    set_return (`“${encodews (`${cs.rwr ().join ('')}`,)}”`);
return exit_rule ("char_string");
},
char_comment : function (lb,cs,rb,) {
enter_rule ("char_comment");
    set_return (`⌈${encodews (`${cs.rwr ().join ('')}`,)}⌉`);
return exit_rule ("char_comment");
},
char_word : function (lb,cs,rb,) {
enter_rule ("char_word");
    set_return (`❲${encodews (`${cs.rwr ().join ('')}`,)}❳`);
return exit_rule ("char_word");
},
char_ident : function (s,) {
enter_rule ("char_ident");
    set_return (`❲${encodews (`${s.rwr ()}`,)}❳`);
return exit_rule ("char_ident");
},
char_any : function (c,) {
enter_rule ("char_any");
    set_return (`${c.rwr ()}`);
return exit_rule ("char_any");
},
stringchar_rec : function (lb,cs,rb,) {
enter_rule ("stringchar_rec");
    set_return (`${lb.rwr ()}${cs.rwr ().join ('')}${rb.rwr ()}`);
return exit_rule ("stringchar_rec");
},
stringchar_other : function (c,) {
enter_rule ("stringchar_other");
    set_return (`${c.rwr ()}`);
return exit_rule ("stringchar_other");
},
commentchar_rec : function (lb,cs,rb,) {
enter_rule ("commentchar_rec");
    set_return (`${lb.rwr ()}${cs.rwr ().join ('')}${rb.rwr ()}`);
return exit_rule ("commentchar_rec");
},
commentchar_other : function (c,) {
enter_rule ("commentchar_other");
    set_return (`${c.rwr ()}`);
return exit_rule ("commentchar_other");
},
wordchar_rec : function (lb,cs,rb,) {
enter_rule ("wordchar_rec");
    set_return (`${lb.rwr ()}${cs.rwr ().join ('')}${rb.rwr ()}`);
return exit_rule ("wordchar_rec");
},
wordchar_other : function (c,) {
enter_rule ("wordchar_other");
    set_return (`${c.rwr ()}`);
return exit_rule ("wordchar_other");
},
id : function (firstc,morecs,) {
enter_rule ("id");
    set_return (`${firstc.rwr ()}${morecs.rwr ().join ('')}`);
return exit_rule ("id");
},
dq : function (c,) {
enter_rule ("dq");
    set_return (`${c.rwr ()}`);
return exit_rule ("dq");
},
nl : function (c,) {
enter_rule ("nl");
    set_return (``);
return exit_rule ("nl");
},
_terminal: function () { return this.sourceString; },
_iter: function (...children) { return children.map(c => c.rwr ()); }
}
