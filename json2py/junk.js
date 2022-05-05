// import sys
// import json
// import html
// import re

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

// def xxx ():
//     s = 'print ("hello")&lt;br&gt;self.send ("out", True)&lt;br&gt;&lt;div&gt;&lt;/div&gt;'
//     # y = html.unescape (s)
//     # print (y)
//     # z = html.unescape (s)
//     # print (z)
//     x = unescapeCode (s)
//     print (x)

// xxx ()

function decode (s) {
    var code = decodeURI (s);
    var code7 = code
	.replace (/&lt;br/g, '<br')
	.replace (/&gt;/g, '>')
	.replace (/&lt;/g, '<')
	.replace (/<pre[^>]*/g, '')
	.replace (/<\/pre>/g, '')
	.replace (/<div>([^<]*)<\/div>/g, '\1\n')
	.replace (/<p ([^>]*)>/g, '')
	.replace (/<\/p>/g, '')
	.replace (/<span ([^<]*)>/g, '')
	.replace (/<\/span>/g, '\n')
	.replace (/<br\/>/g, '\n')
	.replace (/<br>/g, '\n')
	.replace (/&quot;/g, '"')
    ;
    return decodeURI (code7);
}

var s = 'print ("hello")&lt;br&gt;self.send ("out", True)&lt;br&gt;&lt;div&gt;&lt;/div&gt;';
var x = decodeURI (s);
console.log (x);
var y = decode (x);
console.log (y);
