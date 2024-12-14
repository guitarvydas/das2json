: Das2json ^=
  XML Spaces _end

: XML ^=
  Spaces "<" Name Attributes
  [
    | ">": Content "</" Stuff ">"
    | "/>": 
  ]

: Content ^=
  <<<
    Spaces
    [*
      | "</": _break
      | "<mxGeometry ":  mxGeometry
      | "<": XML
      | *: Stuff
    ]
  >>>

: mxGeometry @= XML

: Attributes ^=
  <<<
    [*
      | "style=": Style
      | ">": _break
      | "/>": _break
      | _end: _break
      | *: .
    ]
  >>>

: Style @= "style=" String

: Name ^=
  <<<
    [*
      | " ":   _break
      | "\t": _break
      | "\n": _break
      | ">": _break
      | "<": _break
      | "/>": _break
      | _end: _break
      | *: .
    ]
  >>>

: Stuff ^=
  <<<
    [*
      | ">": _break
      | "<": _break
      | "/>": _break
      | _end: _break
      | *: .
    ]
  >>>

: Spaces ^=
  <<<
    [*
      | " ": .
      | "\t": .
      | "\n": .
      | *: _break
    ]
  >>>

: String ^=
  "\"" NotDquotes "\""

: NotDquotes ^=
  <<<
    [*
      | "\"": _break
      | *: .
    ]
  >>>

: EndMxCell ^= "</mxCell>" Spaces

@ mxGeometry = _ignore_value
@ Style = _ignore_value
