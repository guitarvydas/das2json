// from ../das/pyemit.py ...

// def unescapeCode (s):
//   code = html.unescape (s)
//   # note that <p .../> and <span .../> and <pre .../> are not handled by the
//   # code below (this probably needs a parser - e.g. Ohm-JS - to grok
//   # It looks like we can get away, though, with the simplification below, because
//   # draw.io creates paras and spans and pres in only very specific ways, if
//   # we find a counter-example, it might be necessary to cut over to a
//   # proper parse (e.g. using pfr and .ohm/.glue files))
//   code1a = re.sub (r'<pre([^>]*>)', '', code)
//   code1 = code1a.replace ("</pre>","")
//   code2 = re.sub (r'<div>([^<]*)</div>', r'\1\n', code1, re.MULTILINE)
//   assert (None == re.search (r'<div>', code2)), "<div> not removed (internal error)"
//   code3 = re.sub (r'<p ([^>]*)>', r'', code2)
//   code4 = re.sub (r'</p>', "", code3)
//   code5 = re.sub (r'<span ([^<]*)>', "", code4)
//   code6 = re.sub (r'</span>', "\n", code5)
//   code7a = re.sub (r'<br/>', "\n", code6)
//   code7 = re.sub (r'<br>', "\n", code7a)

//   codefinal = html.unescape (code7)
//   return codefinal
    
exports.decode = function (s) {
    var code = decodeURIComponent (s);
    var code7 = code
	.replace (/&gt;/g, '>')
	.replace (/&lt;/g, '<')
	.replace (/<pre[^>]*/g, '')
	.replace (/<\/pre>/g, '')
	.replace (/<div>([^<]*)<\/div>/g, '\n')
	.replace (/<p ([^>]*)>/g, '')
	.replace (/<\/p>/g, '')
	.replace (/<span ([^<]*)>/g, '')
	.replace (/<\/span>/g, '\n')
	.replace (/<br>/g, '\n')
	.replace (/<br\/>/g, '\n')
	.replace (/&quot;/g, '"')
    ;
    return decodeURIComponent (code7);
}

var comp = {};
exports.reset = function () { comp = {}; }

function put (field, v) {
    if (comp[field]) {
	comp[field].push (v);
    } else {
	comp[field] = [v];
    }
    return "";
}
exports.put = put;
exports.get = function (field) {
    return comp[field].pop ();
}
exports.aget = function (field, prefix) {
    var r = comp[field];
    if (r) {
	return comp[field].join (prefix);
    } else {
	return "";
    }
}

exports.putlines = function (field, s) {
    var a = s.split (/\n/);
    a.forEach (i => put (field, i));
}

exports.pythonize = function (s) {
    return s
	.replace (/ /g, "_")
	.replace (/"/g, "")
}

var counter = 0;
exports.gensym = function () {
    counter += 1;
    return counter.toString ();
}
function getsym  () {
    return counter.toString ();
}
exports.getsym = getsym;

exports.formatChildMapEntry = function (n) {
    put ("children", `${n}:child${getsym ()}`);
    return '';
}
