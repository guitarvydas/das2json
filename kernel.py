

import sys
import re
import subprocess
import shlex
import os
import json
from collections import deque
                                                            #line 1#line 2
counter =  0                                                #line 3#line 4
digits = [ "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", "₁₁", "₁₂", "₁₃", "₁₄", "₁₅", "₁₆", "₁₇", "₁₈", "₁₉", "₂₀", "₂₁", "₂₂", "₂₃", "₂₄", "₂₅", "₂₆", "₂₇", "₂₈", "₂₉"]#line 11#line 12#line 13
def gensymbol (s):                                          #line 14
    global counter                                          #line 15
    name_with_id =  str( s) + subscripted_digit ( counter)  #line 16
    counter =  counter+ 1                                   #line 17
    return  name_with_id                                    #line 18#line 19#line 20

def subscripted_digit (n):                                  #line 21
    global digits                                           #line 22
    if ( n >=  0 and  n <=  29):                            #line 23
        return  digits [ n]                                 #line 24
    else:                                                   #line 25
        return  str( "₊") +  n                              #line 26#line 27#line 28#line 29

class Datum:
    def __init__ (self,):                                   #line 30
        self.data =  None                                   #line 31
        self.clone =  None                                  #line 32
        self.reclaim =  None                                #line 33
        self.srepr =  None                                  #line 34
        self.kind =  None                                   #line 35
        self.raw =  None                                    #line 36#line 37
                                                            #line 38
def new_datum_string (s):                                   #line 39
    d =  Datum ()                                           #line 40
    d.data =  s                                             #line 41
    d.clone =  lambda : clone_datum_string ( d)             #line 42
    d.reclaim =  lambda : reclaim_datum_string ( d)         #line 43
    d.srepr =  lambda : srepr_datum_string ( d)             #line 44
    d.raw = bytearray ( d.data,"UTF_8")                     #line 45
    d.kind =  lambda :  "string"                            #line 46
    return  d                                               #line 47#line 48#line 49

def clone_datum_string (d):                                 #line 50
    newd = new_datum_string ( d.data)                       #line 51
    return  newd                                            #line 52#line 53#line 54

def reclaim_datum_string (src):                             #line 55
    pass                                                    #line 56#line 57#line 58

def srepr_datum_string (d):                                 #line 59
    return  d.data                                          #line 60#line 61#line 62

def new_datum_bang ():                                      #line 63
    p =  Datum ()                                           #line 64
    p.data =  True                                          #line 65
    p.clone =  lambda : clone_datum_bang ( p)               #line 66
    p.reclaim =  lambda : reclaim_datum_bang ( p)           #line 67
    p.srepr =  lambda : srepr_datum_bang ()                 #line 68
    p.raw =  lambda : raw_datum_bang ()                     #line 69
    p.kind =  lambda :  "bang"                              #line 70
    return  p                                               #line 71#line 72#line 73

def clone_datum_bang (d):                                   #line 74
    return new_datum_bang ()                                #line 75#line 76#line 77

def reclaim_datum_bang (d):                                 #line 78
    pass                                                    #line 79#line 80#line 81

def srepr_datum_bang ():                                    #line 82
    return  "!"                                             #line 83#line 84#line 85

def raw_datum_bang ():                                      #line 86
    return []                                               #line 87#line 88#line 89

def new_datum_tick ():                                      #line 90
    p = new_datum_bang ()                                   #line 91
    p.kind =  lambda :  "tick"                              #line 92
    p.clone =  lambda : new_datum_tick ()                   #line 93
    p.srepr =  lambda : srepr_datum_tick ()                 #line 94
    p.raw =  lambda : raw_datum_tick ()                     #line 95
    return  p                                               #line 96#line 97#line 98

def srepr_datum_tick ():                                    #line 99
    return  "."                                             #line 100#line 101#line 102

def raw_datum_tick ():                                      #line 103
    return []                                               #line 104#line 105#line 106

def new_datum_bytes (b):                                    #line 107
    p =  Datum ()                                           #line 108
    p.data =  b                                             #line 109
    p.clone =  lambda : clone_datum_bytes ( p)              #line 110
    p.reclaim =  lambda : reclaim_datum_bytes ( p)          #line 111
    p.srepr =  lambda : srepr_datum_bytes ( b)              #line 112
    p.raw =  lambda : raw_datum_bytes ( b)                  #line 113
    p.kind =  lambda :  "bytes"                             #line 114
    return  p                                               #line 115#line 116#line 117

def clone_datum_bytes (src):                                #line 118
    p =  Datum ()                                           #line 119
    p.clone =  src.clone                                    #line 120
    p.reclaim =  src.reclaim                                #line 121
    p.srepr =  src.srepr                                    #line 122
    p.raw =  src.raw                                        #line 123
    p.kind =  src.kind                                      #line 124
    p.data =  src.clone ()                                  #line 125
    return  p                                               #line 126#line 127#line 128

def reclaim_datum_bytes (src):                              #line 129
    pass                                                    #line 130#line 131#line 132

def srepr_datum_bytes (d):                                  #line 133
    return  d.data.decode ( "UTF_8")                        #line 134#line 135

def raw_datum_bytes (d):                                    #line 136
    return  d.data                                          #line 137#line 138#line 139

def new_datum_handle (h):                                   #line 140
    return new_datum_int ( h)                               #line 141#line 142#line 143

def new_datum_int (i):                                      #line 144
    p =  Datum ()                                           #line 145
    p.data =  i                                             #line 146
    p.clone =  lambda : clone_int ( i)                      #line 147
    p.reclaim =  lambda : reclaim_int ( i)                  #line 148
    p.srepr =  lambda : srepr_datum_int ( i)                #line 149
    p.raw =  lambda : raw_datum_int ( i)                    #line 150
    p.kind =  lambda :  "int"                               #line 151
    return  p                                               #line 152#line 153#line 154

def clone_int (i):                                          #line 155
    p = new_datum_int ( i)                                  #line 156
    return  p                                               #line 157#line 158#line 159

def reclaim_int (src):                                      #line 160
    pass                                                    #line 161#line 162#line 163

def srepr_datum_int (i):                                    #line 164
    return str ( i)                                         #line 165#line 166#line 167

def raw_datum_int (i):                                      #line 168
    return  i                                               #line 169#line 170#line 171

# Message passed to a leaf component.                       #line 172
#                                                           #line 173
# `port` refers to the name of the incoming or outgoing port of this component.#line 174
# `datum` is the data attached to this message.             #line 175
class Message:
    def __init__ (self,):                                   #line 176
        self.port =  None                                   #line 177
        self.datum =  None                                  #line 178#line 179
                                                            #line 180
def clone_port (s):                                         #line 181
    return clone_string ( s)                                #line 182#line 183#line 184

# Utility for making a `Message`. Used to safely “seed“ messages#line 185
# entering the very top of a network.                       #line 186
def make_message (port,datum):                              #line 187
    p = clone_string ( port)                                #line 188
    m =  Message ()                                         #line 189
    m.port =  p                                             #line 190
    m.datum =  datum.clone ()                               #line 191
    return  m                                               #line 192#line 193#line 194

# Clones a message. Primarily used internally for “fanning out“ a message to multiple destinations.#line 195
def message_clone (msg):                                    #line 196
    m =  Message ()                                         #line 197
    m.port = clone_port ( msg.port)                         #line 198
    m.datum =  msg.datum.clone ()                           #line 199
    return  m                                               #line 200#line 201#line 202

# Frees a message.                                          #line 203
def destroy_message (msg):                                  #line 204
    # during debug, dont destroy any message, since we want to trace messages, thus, we need to persist ancestor messages#line 205
    pass                                                    #line 206#line 207#line 208

def destroy_datum (msg):                                    #line 209
    pass                                                    #line 210#line 211#line 212

def destroy_port (msg):                                     #line 213
    pass                                                    #line 214#line 215#line 216

#                                                           #line 217
def format_message (m):                                     #line 218
    if  m ==  None:                                         #line 219
        return  "ϕ"                                         #line 220
    else:                                                   #line 221
        return  str( "⟪") +  str( m.port) +  str( "⦂") +  str( m.datum.srepr ()) +  "⟫"    #line 225#line 226#line 227#line 228
                                                            #line 229
enumDown =  0                                               #line 230
enumAcross =  1                                             #line 231
enumUp =  2                                                 #line 232
enumThrough =  3                                            #line 233#line 234
def create_down_connector (container,proto_conn,connectors,children_by_id):#line 235
    # JSON: {;dir': 0, 'source': {'name': '', 'id': 0}, 'source_port': '', 'target': {'name': 'Echo', 'id': 12}, 'target_port': ''},#line 236
    connector =  Connector ()                               #line 237
    connector.direction =  "down"                           #line 238
    connector.sender = mkSender ( container.name, container, proto_conn [ "source_port"])#line 239
    target_proto =  proto_conn [ "target"]                  #line 240
    id_proto =  target_proto [ "id"]                        #line 241
    target_component =  children_by_id [id_proto]           #line 242
    if ( target_component ==  None):                        #line 243
        load_error ( str( "internal error: .Down connection target internal error ") + ( proto_conn [ "target"]) [ "name"] )#line 244
    else:                                                   #line 245
        connector.receiver = mkReceiver ( target_component.name, target_component, proto_conn [ "target_port"], target_component.inq)#line 246#line 247
    return  connector                                       #line 248#line 249#line 250

def create_across_connector (container,proto_conn,connectors,children_by_id):#line 251
    connector =  Connector ()                               #line 252
    connector.direction =  "across"                         #line 253
    source_component =  children_by_id [(( proto_conn [ "source"]) [ "id"])]#line 254
    target_component =  children_by_id [(( proto_conn [ "target"]) [ "id"])]#line 255
    if  source_component ==  None:                          #line 256
        load_error ( str( "internal error: .Across connection source not ok ") + ( proto_conn [ "source"]) [ "name"] )#line 257
    else:                                                   #line 258
        connector.sender = mkSender ( source_component.name, source_component, proto_conn [ "source_port"])#line 259
        if  target_component ==  None:                      #line 260
            load_error ( str( "internal error: .Across connection target not ok ") + ( proto_conn [ "target"]) [ "name"] )#line 261
        else:                                               #line 262
            connector.receiver = mkReceiver ( target_component.name, target_component, proto_conn [ "target_port"], target_component.inq)#line 263#line 264#line 265
    return  connector                                       #line 266#line 267#line 268

def create_up_connector (container,proto_conn,connectors,children_by_id):#line 269
    connector =  Connector ()                               #line 270
    connector.direction =  "up"                             #line 271
    source_component =  children_by_id [(( proto_conn [ "source"]) [ "id"])]#line 272
    if  source_component ==  None:                          #line 273
        print ( str( "internal error: .Up connection source not ok ") + ( proto_conn [ "source"]) [ "name"] )#line 274
    else:                                                   #line 275
        connector.sender = mkSender ( source_component.name, source_component, proto_conn [ "source_port"])#line 276
        connector.receiver = mkReceiver ( container.name, container, proto_conn [ "target_port"], container.outq)#line 277#line 278
    return  connector                                       #line 279#line 280#line 281

def create_through_connector (container,proto_conn,connectors,children_by_id):#line 282
    connector =  Connector ()                               #line 283
    connector.direction =  "through"                        #line 284
    connector.sender = mkSender ( container.name, container, proto_conn [ "source_port"])#line 285
    connector.receiver = mkReceiver ( container.name, container, proto_conn [ "target_port"], container.outq)#line 286
    return  connector                                       #line 287#line 288#line 289
                                                            #line 290
def container_instantiator (reg,owner,container_name,desc): #line 291
    global enumDown, enumUp, enumAcross, enumThrough        #line 292
    container = make_container ( container_name, owner)     #line 293
    children = []                                           #line 294
    children_by_id = {}
    # not strictly necessary, but, we can remove 1 runtime lookup by “compiling it out“ here#line 295
    # collect children                                      #line 296
    for child_desc in  desc [ "children"]:                  #line 297
        child_instance = get_component_instance ( reg, child_desc [ "name"], container)#line 298
        children.append ( child_instance)                   #line 299
        id =  child_desc [ "id"]                            #line 300
        children_by_id [id] =  child_instance               #line 301#line 302#line 303
    container.children =  children                          #line 304#line 305
    connectors = []                                         #line 306
    for proto_conn in  desc [ "connections"]:               #line 307
        connector =  Connector ()                           #line 308
        if  proto_conn [ "dir"] ==  enumDown:               #line 309
            connectors.append (create_down_connector ( container, proto_conn, connectors, children_by_id)) #line 310
        elif  proto_conn [ "dir"] ==  enumAcross:           #line 311
            connectors.append (create_across_connector ( container, proto_conn, connectors, children_by_id)) #line 312
        elif  proto_conn [ "dir"] ==  enumUp:               #line 313
            connectors.append (create_up_connector ( container, proto_conn, connectors, children_by_id)) #line 314
        elif  proto_conn [ "dir"] ==  enumThrough:          #line 315
            connectors.append (create_through_connector ( container, proto_conn, connectors, children_by_id)) #line 316#line 317#line 318
    container.connections =  connectors                     #line 319
    return  container                                       #line 320#line 321#line 322

# The default handler for container components.             #line 323
def container_handler (container,message):                  #line 324
    route ( container, container, message)
    # references to 'self' are replaced by the container during instantiation#line 325
    while any_child_ready ( container):                     #line 326
        step_children ( container, message)                 #line 327#line 328#line 329

# Frees the given container and associated data.            #line 330
def destroy_container (eh):                                 #line 331
    pass                                                    #line 332#line 333#line 334

# Routing connection for a container component. The `direction` field has#line 335
# no affect on the default message routing system _ it is there for debugging#line 336
# purposes, or for reading by other tools.                  #line 337#line 338
class Connector:
    def __init__ (self,):                                   #line 339
        self.direction =  None # down, across, up, through  #line 340
        self.sender =  None                                 #line 341
        self.receiver =  None                               #line 342#line 343
                                                            #line 344
# `Sender` is used to “pattern match“ which `Receiver` a message should go to,#line 345
# based on component ID (pointer) and port name.            #line 346#line 347
class Sender:
    def __init__ (self,):                                   #line 348
        self.name =  None                                   #line 349
        self.component =  None                              #line 350
        self.port =  None                                   #line 351#line 352
                                                            #line 353#line 354#line 355
# `Receiver` is a handle to a destination queue, and a `port` name to assign#line 356
# to incoming messages to this queue.                       #line 357#line 358
class Receiver:
    def __init__ (self,):                                   #line 359
        self.name =  None                                   #line 360
        self.queue =  None                                  #line 361
        self.port =  None                                   #line 362
        self.component =  None                              #line 363#line 364
                                                            #line 365
def mkSender (name,component,port):                         #line 366
    s =  Sender ()                                          #line 367
    s.name =  name                                          #line 368
    s.component =  component                                #line 369
    s.port =  port                                          #line 370
    return  s                                               #line 371#line 372#line 373

def mkReceiver (name,component,port,q):                     #line 374
    r =  Receiver ()                                        #line 375
    r.name =  name                                          #line 376
    r.component =  component                                #line 377
    r.port =  port                                          #line 378
    # We need a way to determine which queue to target. "Down" and "Across" go to inq, "Up" and "Through" go to outq.#line 379
    r.queue =  q                                            #line 380
    return  r                                               #line 381#line 382#line 383

# Checks if two senders match, by pointer equality and port name matching.#line 384
def sender_eq (s1,s2):                                      #line 385
    same_components = ( s1.component ==  s2.component)      #line 386
    same_ports = ( s1.port ==  s2.port)                     #line 387
    return  same_components and  same_ports                 #line 388#line 389#line 390

# Delivers the given message to the receiver of this connector.#line 391#line 392
def deposit (parent,conn,message):                          #line 393
    new_message = make_message ( conn.receiver.port, message.datum)#line 394
    push_message ( parent, conn.receiver.component, conn.receiver.queue, new_message)#line 395#line 396#line 397

def force_tick (parent,eh):                                 #line 398
    tick_msg = make_message ( ".",new_datum_tick ())        #line 399
    push_message ( parent, eh, eh.inq, tick_msg)            #line 400
    return  tick_msg                                        #line 401#line 402#line 403

def push_message (parent,receiver,inq,m):                   #line 404
    inq.append ( m)                                         #line 405
    parent.visit_ordering.append ( receiver)                #line 406#line 407#line 408

def is_self (child,container):                              #line 409
    # in an earlier version “self“ was denoted as ϕ         #line 410
    return  child ==  container                             #line 411#line 412#line 413

def step_child (child,msg):                                 #line 414
    before_state =  child.state                             #line 415
    child.handler ( child, msg)                             #line 416
    after_state =  child.state                              #line 417
    return [ before_state ==  "idle" and  after_state!= "idle", before_state!= "idle" and  after_state!= "idle", before_state!= "idle" and  after_state ==  "idle"]#line 420#line 421#line 422

def step_children (container,causingMessage):               #line 423
    container.state =  "idle"                               #line 424
    for child in  list ( container.visit_ordering):         #line 425
        # child = container represents self, skip it        #line 426
        if (not (is_self ( child, container))):             #line 427
            if (not ((0==len( child.inq)))):                #line 428
                msg =  child.inq.popleft ()                 #line 429
                began_long_run =  None                      #line 430
                continued_long_run =  None                  #line 431
                ended_long_run =  None                      #line 432
                [ began_long_run, continued_long_run, ended_long_run] = step_child ( child, msg)#line 433
                if  began_long_run:                         #line 434
                    pass                                    #line 435
                elif  continued_long_run:                   #line 436
                    pass                                    #line 437
                elif  ended_long_run:                       #line 438
                    pass                                    #line 439#line 440
                destroy_message ( msg)                      #line 441
            else:                                           #line 442
                if  child.state!= "idle":                   #line 443
                    msg = force_tick ( container, child)    #line 444
                    child.handler ( child, msg)             #line 445
                    destroy_message ( msg)                  #line 446#line 447
            if  child.state ==  "active":                   #line 448
                # if child remains active, then the container must remain active and must propagate “ticks“ to child#line 449
                container.state =  "active"                 #line 450#line 451
            while (not ((0==len( child.outq)))):            #line 452
                msg =  child.outq.popleft ()                #line 453
                route ( container, child, msg)              #line 454
                destroy_message ( msg)                      #line 455#line 456#line 457#line 458#line 459

def attempt_tick (parent,eh):                               #line 460
    if  eh.state!= "idle":                                  #line 461
        force_tick ( parent, eh)                            #line 462#line 463#line 464

def is_tick (msg):                                          #line 465
    return  "tick" ==  msg.datum.kind ()                    #line 466#line 467#line 468

# Routes a single message to all matching destinations, according to#line 469
# the container's connection network.                       #line 470#line 471
def route (container,from_component,message):               #line 472
    was_sent =  False
    # for checking that output went somewhere (at least during bootstrap)#line 473
    fromname =  ""                                          #line 474
    if is_tick ( message):                                  #line 475
        for child in  container.children:                   #line 476
            attempt_tick ( container, child)                #line 477
        was_sent =  True                                    #line 478
    else:                                                   #line 479
        if (not (is_self ( from_component, container))):    #line 480
            fromname =  from_component.name                 #line 481
        from_sender = mkSender ( fromname, from_component, message.port)#line 482#line 483
        for connector in  container.connections:            #line 484
            if sender_eq ( from_sender, connector.sender):  #line 485
                deposit ( container, connector, message)    #line 486
                was_sent =  True                            #line 487
    if not ( was_sent):                                     #line 488
        print ( "\n\n*** Error: ***")                       #line 489
        print ( "***")                                      #line 490
        print ( str( container.name) +  str( ": message '") +  str( message.port) +  str( "' from ") +  str( fromname) +  " dropped on floor..."     )#line 491
        print ( "***")                                      #line 492
        exit ()                                             #line 493#line 494#line 495#line 496

def any_child_ready (container):                            #line 497
    for child in  container.children:                       #line 498
        if child_is_ready ( child):                         #line 499
            return  True                                    #line 500
    return  False                                           #line 501#line 502#line 503

def child_is_ready (eh):                                    #line 504
    return (not ((0==len( eh.outq)))) or (not ((0==len( eh.inq)))) or ( eh.state!= "idle") or (any_child_ready ( eh))#line 505#line 506#line 507

def append_routing_descriptor (container,desc):             #line 508
    container.routings.append ( desc)                       #line 509#line 510#line 511

def container_injector (container,message):                 #line 512
    container_handler ( container, message)                 #line 513#line 514#line 515






                                                            #line 1#line 2#line 3
class Component_Registry:
    def __init__ (self,):                                   #line 4
        self.templates = {}                                 #line 5#line 6
                                                            #line 7
class Template:
    def __init__ (self,):                                   #line 8
        self.name =  None                                   #line 9
        self.template_data =  None                          #line 10
        self.instantiator =  None                           #line 11#line 12
                                                            #line 13
def mkTemplate (name,template_data,instantiator):           #line 14
    templ =  Template ()                                    #line 15
    templ.name =  name                                      #line 16
    templ.template_data =  template_data                    #line 17
    templ.instantiator =  instantiator                      #line 18
    return  templ                                           #line 19#line 20#line 21

def read_and_convert_json_file (pathname,filename):         #line 22

    try:
        fil = open(filename, "r")
        json_data = fil.read()
        routings = json.loads(json_data)
        fil.close ()
        return routings
    except FileNotFoundError:
        print (f"File not found: '{filename}'")
        return None
    except json.JSONDecodeError as e:
        print ("Error decoding JSON in file: '{e}'")
        return None
                                                            #line 23#line 24#line 25

def json2internal (pathname,container_xml):                 #line 26
    fname =  os.path.basename ( container_xml)              #line 27
    routings = read_and_convert_json_file ( pathname, fname)#line 28
    return  routings                                        #line 29#line 30#line 31

def delete_decls (d):                                       #line 32
    pass                                                    #line 33#line 34#line 35

def make_component_registry ():                             #line 36
    return  Component_Registry ()                           #line 37#line 38#line 39

def register_component (reg,template):
    return abstracted_register_component ( reg, template, False)#line 40

def register_component_allow_overwriting (reg,template):
    return abstracted_register_component ( reg, template, True)#line 41#line 42

def abstracted_register_component (reg,template,ok_to_overwrite):#line 43
    name = mangle_name ( template.name)                     #line 44
    if  reg!= None and  name in  reg.templates and not  ok_to_overwrite:#line 45
        load_error ( str( "Component /") +  str( template.name) +  "/ already declared"  )#line 46
        return  reg                                         #line 47
    else:                                                   #line 48
        reg.templates [name] =  template                    #line 49
        return  reg                                         #line 50#line 51#line 52#line 53

def get_component_instance (reg,full_name,owner):           #line 54
    template_name = mangle_name ( full_name)                #line 55
    if  template_name in  reg.templates:                    #line 56
        template =  reg.templates [template_name]           #line 57
        if ( template ==  None):                            #line 58
            load_error ( str( "Registry Error (A): Can;t find component /") +  str( template_name) +  "/"  )#line 59
            return  None                                    #line 60
        else:                                               #line 61
            owner_name =  ""                                #line 62
            instance_name =  template_name                  #line 63
            if  None!= owner:                               #line 64
                owner_name =  owner.name                    #line 65
                instance_name =  str( owner_name) +  str( ".") +  template_name  #line 66
            else:                                           #line 67
                instance_name =  template_name              #line 68
            instance =  template.instantiator ( reg, owner, instance_name, template.template_data)#line 69
            return  instance                                #line 70
    else:                                                   #line 71
        load_error ( str( "Registry Error (B): Can't find component /") +  str( template_name) +  "/"  )#line 72
        return  None                                        #line 73#line 74#line 75

def dump_registry (reg):                                    #line 76
    nl ()                                                   #line 77
    print ( "*** PALETTE ***")                              #line 78
    for c in  reg.templates:                                #line 79
        print ( c.name)                                     #line 80
    print ( "***************")                              #line 81
    nl ()                                                   #line 82#line 83#line 84

def print_stats (reg):                                      #line 85
    print ( str( "registry statistics: ") +  reg.stats )    #line 86#line 87#line 88

def mangle_name (s):                                        #line 89
    # trim name to remove code from Container component names _ deferred until later (or never)#line 90
    return  s                                               #line 91#line 92#line 93

def generate_shell_components (reg,container_list):         #line 94
    # [                                                     #line 95
    #     {'file': 'simple0d.drawio', 'name': 'main', 'children': [{'name': 'Echo', 'id': 5}], 'connections': [...]},#line 96
    #     {'file': 'simple0d.drawio', 'name': '...', 'children': [], 'connections': []}#line 97
    # ]                                                     #line 98
    if  None!= container_list:                              #line 99
        for diagram in  container_list:                     #line 100
            # loop through every component in the diagram and look for names that start with “$“ or “'“ #line 101
            # {'file': 'simple0d.drawio', 'name': 'main', 'children': [{'name': 'Echo', 'id': 5}], 'connections': [...]},#line 102
            for child_descriptor in  diagram [ "children"]: #line 103
                if first_char_is ( child_descriptor [ "name"], "$"):#line 104
                    name =  child_descriptor [ "name"]      #line 105
                    cmd =   name[1:] .strip ()              #line 106
                    generated_leaf = mkTemplate ( name, cmd, shell_out_instantiate)#line 107
                    register_component ( reg, generated_leaf)#line 108
                elif first_char_is ( child_descriptor [ "name"], "'"):#line 109
                    name =  child_descriptor [ "name"]      #line 110
                    s =   name[1:]                          #line 111
                    generated_leaf = mkTemplate ( name, s, string_constant_instantiate)#line 112
                    register_component_allow_overwriting ( reg, generated_leaf)#line 113#line 114#line 115#line 116#line 117
    return  reg                                             #line 118#line 119#line 120

def first_char (s):                                         #line 121
    return   s[0]                                           #line 122#line 123#line 124

def first_char_is (s,c):                                    #line 125
    return  c == first_char ( s)                            #line 126#line 127#line 128
                                                            #line 129
# TODO: #run_command needs to be rewritten to use the low_level “shell_out“ component, this can be done solely as a diagram without using python code here#line 130
# I'll keep it for now, during bootstrapping, since it mimics what is done in the Odin prototype _ both need to be revamped#line 131#line 132#line 133
# Data for an asyncronous component _ effectively, a function with input#line 134
# and output queues of messages.                            #line 135
#                                                           #line 136
# Components can either be a user_supplied function (“lea“), or a “container“#line 137
# that routes messages to child components according to a list of connections#line 138
# that serve as a message routing table.                    #line 139
#                                                           #line 140
# Child components themselves can be leaves or other containers.#line 141
#                                                           #line 142
# `handler` invokes the code that is attached to this component.#line 143
#                                                           #line 144
# `instance_data` is a pointer to instance data that the `leaf_handler`#line 145
# function may want whenever it is invoked again.           #line 146
#                                                           #line 147#line 148
# Eh_States :: enum { idle, active }                        #line 149
class Eh:
    def __init__ (self,):                                   #line 150
        self.name =  ""                                     #line 151
        self.inq =  deque ([])                              #line 152
        self.outq =  deque ([])                             #line 153
        self.owner =  None                                  #line 154
        self.children = []                                  #line 155
        self.visit_ordering =  deque ([])                   #line 156
        self.connections = []                               #line 157
        self.routings =  deque ([])                         #line 158
        self.handler =  None                                #line 159
        self.finject =  None                                #line 160
        self.instance_data =  None                          #line 161
        self.state =  "idle"                                #line 162# bootstrap debugging#line 163
        self.kind =  None # enum { container, leaf, }       #line 164#line 165
                                                            #line 166
# Creates a component that acts as a container. It is the same as a `Eh` instance#line 167
# whose handler function is `container_handler`.            #line 168
def make_container (name,owner):                            #line 169
    eh =  Eh ()                                             #line 170
    eh.name =  name                                         #line 171
    eh.owner =  owner                                       #line 172
    eh.handler =  container_handler                         #line 173
    eh.finject =  container_injector                        #line 174
    eh.state =  "idle"                                      #line 175
    eh.kind =  "container"                                  #line 176
    return  eh                                              #line 177#line 178#line 179

# Creates a new leaf component out of a handler function, and a data parameter#line 180
# that will be passed back to your handler when called.     #line 181#line 182
def make_leaf (name,owner,instance_data,handler):           #line 183
    eh =  Eh ()                                             #line 184
    eh.name =  str( owner.name) +  str( ".") +  name        #line 185
    eh.owner =  owner                                       #line 186
    eh.handler =  handler                                   #line 187
    eh.instance_data =  instance_data                       #line 188
    eh.state =  "idle"                                      #line 189
    eh.kind =  "leaf"                                       #line 190
    return  eh                                              #line 191#line 192#line 193

# Sends a message on the given `port` with `data`, placing it on the output#line 194
# of the given component.                                   #line 195#line 196
def send (eh,port,datum,causingMessage):                    #line 197
    msg = make_message ( port, datum)                       #line 198
    put_output ( eh, msg)                                   #line 199#line 200#line 201

def send_string (eh,port,s,causingMessage):                 #line 202
    datum = new_datum_string ( s)                           #line 203
    msg = make_message ( port, datum)                       #line 204
    put_output ( eh, msg)                                   #line 205#line 206#line 207

def forward (eh,port,msg):                                  #line 208
    fwdmsg = make_message ( port, msg.datum)                #line 209
    put_output ( eh, msg)                                   #line 210#line 211#line 212

def inject (eh,msg):                                        #line 213
    eh.finject ( eh, msg)                                   #line 214#line 215#line 216

# Returns a list of all output messages on a container.     #line 217
# For testing / debugging purposes.                         #line 218#line 219
def output_list (eh):                                       #line 220
    return  eh.outq                                         #line 221#line 222#line 223

# Utility for printing an array of messages.                #line 224
def print_output_list (eh):                                 #line 225
    for m in  list ( eh.outq):                              #line 226
        print (format_message ( m))                         #line 227#line 228#line 229

def spaces (n):                                             #line 230
    s =  ""                                                 #line 231
    for i in range( n):                                     #line 232
        s =  s+ " "                                         #line 233
    return  s                                               #line 234#line 235#line 236

def set_active (eh):                                        #line 237
    eh.state =  "active"                                    #line 238#line 239#line 240

def set_idle (eh):                                          #line 241
    eh.state =  "idle"                                      #line 242#line 243#line 244

# Utility for printing a specific output message.           #line 245#line 246
def fetch_first_output (eh,port):                           #line 247
    for msg in  list ( eh.outq):                            #line 248
        if ( msg.port ==  port):                            #line 249
            return  msg.datum                               #line 250
    return  None                                            #line 251#line 252#line 253

def print_specific_output (eh,port):                        #line 254
    # port ∷ “”                                             #line 255
    datum = fetch_first_output ( eh, port)                  #line 256
    print ( datum.srepr ())                                 #line 257#line 258

def print_specific_output_to_stderr (eh,port):              #line 259
    # port ∷ “”                                             #line 260
    datum = fetch_first_output ( eh, port)                  #line 261
    # I don't remember why I found it useful to print to stderr during bootstrapping, so I've left it in...#line 262
    print ( datum.srepr (), file=sys.stderr)                #line 263#line 264#line 265

def put_output (eh,msg):                                    #line 266
    eh.outq.append ( msg)                                   #line 267#line 268#line 269

root_project =  ""                                          #line 270
root_0D =  ""                                               #line 271#line 272
def set_environment (rproject,r0D):                         #line 273
    global root_project                                     #line 274
    global root_0D                                          #line 275
    root_project =  rproject                                #line 276
    root_0D =  r0D                                          #line 277#line 278#line 279

def probe_instantiate (reg,owner,name,template_data):       #line 280
    name_with_id = gensymbol ( "?")                         #line 281
    return make_leaf ( name_with_id, owner, None, probe_handler)#line 282#line 283

def probeA_instantiate (reg,owner,name,template_data):      #line 284
    name_with_id = gensymbol ( "?A")                        #line 285
    return make_leaf ( name_with_id, owner, None, probe_handler)#line 286#line 287#line 288

def probeB_instantiate (reg,owner,name,template_data):      #line 289
    name_with_id = gensymbol ( "?B")                        #line 290
    return make_leaf ( name_with_id, owner, None, probe_handler)#line 291#line 292#line 293

def probeC_instantiate (reg,owner,name,template_data):      #line 294
    name_with_id = gensymbol ( "?C")                        #line 295
    return make_leaf ( name_with_id, owner, None, probe_handler)#line 296#line 297#line 298

def probe_handler (eh,msg):                                 #line 299
    s =  msg.datum.srepr ()                                 #line 300
    print ( str( "... probe ") +  str( eh.name) +  str( ": ") +  s   , file=sys.stderr)#line 301#line 302#line 303

def trash_instantiate (reg,owner,name,template_data):       #line 304
    name_with_id = gensymbol ( "trash")                     #line 305
    return make_leaf ( name_with_id, owner, None, trash_handler)#line 306#line 307#line 308

def trash_handler (eh,msg):                                 #line 309
    # to appease dumped_on_floor checker                    #line 310
    pass                                                    #line 311#line 312

class TwoMessages:
    def __init__ (self,):                                   #line 313
        self.firstmsg =  None                               #line 314
        self.secondmsg =  None                              #line 315#line 316
                                                            #line 317
# Deracer_States :: enum { idle, waitingForFirstmsg, waitingForSecondmsg }#line 318
class Deracer_Instance_Data:
    def __init__ (self,):                                   #line 319
        self.state =  None                                  #line 320
        self.buffer =  None                                 #line 321#line 322
                                                            #line 323
def reclaim_Buffers_from_heap (inst):                       #line 324
    pass                                                    #line 325#line 326#line 327

def deracer_instantiate (reg,owner,name,template_data):     #line 328
    name_with_id = gensymbol ( "deracer")                   #line 329
    inst =  Deracer_Instance_Data ()                        #line 330
    inst.state =  "idle"                                    #line 331
    inst.buffer =  TwoMessages ()                           #line 332
    eh = make_leaf ( name_with_id, owner, inst, deracer_handler)#line 333
    return  eh                                              #line 334#line 335#line 336

def send_firstmsg_then_secondmsg (eh,inst):                 #line 337
    forward ( eh, "1", inst.buffer.firstmsg)                #line 338
    forward ( eh, "2", inst.buffer.secondmsg)               #line 339
    reclaim_Buffers_from_heap ( inst)                       #line 340#line 341#line 342

def deracer_handler (eh,msg):                               #line 343
    inst =  eh.instance_data                                #line 344
    if  inst.state ==  "idle":                              #line 345
        if  "1" ==  msg.port:                               #line 346
            inst.buffer.firstmsg =  msg                     #line 347
            inst.state =  "waitingForSecondmsg"             #line 348
        elif  "2" ==  msg.port:                             #line 349
            inst.buffer.secondmsg =  msg                    #line 350
            inst.state =  "waitingForFirstmsg"              #line 351
        else:                                               #line 352
            runtime_error ( str( "bad msg.port (case A) for deracer ") +  msg.port )#line 353
    elif  inst.state ==  "waitingForFirstmsg":              #line 354
        if  "1" ==  msg.port:                               #line 355
            inst.buffer.firstmsg =  msg                     #line 356
            send_firstmsg_then_secondmsg ( eh, inst)        #line 357
            inst.state =  "idle"                            #line 358
        else:                                               #line 359
            runtime_error ( str( "bad msg.port (case B) for deracer ") +  msg.port )#line 360
    elif  inst.state ==  "waitingForSecondmsg":             #line 361
        if  "2" ==  msg.port:                               #line 362
            inst.buffer.secondmsg =  msg                    #line 363
            send_firstmsg_then_secondmsg ( eh, inst)        #line 364
            inst.state =  "idle"                            #line 365
        else:                                               #line 366
            runtime_error ( str( "bad msg.port (case C) for deracer ") +  msg.port )#line 367
    else:                                                   #line 368
        runtime_error ( "bad state for deracer {eh.state}") #line 369#line 370#line 371

def low_level_read_text_file_instantiate (reg,owner,name,template_data):#line 372
    name_with_id = gensymbol ( "Low Level Read Text File")  #line 373
    return make_leaf ( name_with_id, owner, None, low_level_read_text_file_handler)#line 374#line 375#line 376

def low_level_read_text_file_handler (eh,msg):              #line 377
    fname =  msg.datum.srepr ()                             #line 378

    try:
        f = open (fname)
    except Exception as e:
        f = None
    if f != None:
        data = f.read ()
        if data!= None:
            send_string (eh, "", data, msg)
        else:
            send_string (eh, "✗", f"read error on file '{fname}'", msg)
        f.close ()
    else:
        send_string (eh, "✗", f"open error on file '{fname}'", msg)
                                                            #line 379#line 380#line 381

def ensure_string_datum_instantiate (reg,owner,name,template_data):#line 382
    name_with_id = gensymbol ( "Ensure String Datum")       #line 383
    return make_leaf ( name_with_id, owner, None, ensure_string_datum_handler)#line 384#line 385#line 386

def ensure_string_datum_handler (eh,msg):                   #line 387
    if  "string" ==  msg.datum.kind ():                     #line 388
        forward ( eh, "", msg)                              #line 389
    else:                                                   #line 390
        emsg =  str( "*** ensure: type error (expected a string datum) but got ") +  msg.datum #line 391
        send_string ( eh, "✗", emsg, msg)                   #line 392#line 393#line 394

class Syncfilewrite_Data:
    def __init__ (self,):                                   #line 395
        self.filename =  ""                                 #line 396#line 397
                                                            #line 398
# temp copy for bootstrap, sends “done“ (error during bootstrap if not wired)#line 399
def syncfilewrite_instantiate (reg,owner,name,template_data):#line 400
    name_with_id = gensymbol ( "syncfilewrite")             #line 401
    inst =  Syncfilewrite_Data ()                           #line 402
    return make_leaf ( name_with_id, owner, inst, syncfilewrite_handler)#line 403#line 404#line 405

def syncfilewrite_handler (eh,msg):                         #line 406
    inst =  eh.instance_data                                #line 407
    if  "filename" ==  msg.port:                            #line 408
        inst.filename =  msg.datum.srepr ()                 #line 409
    elif  "input" ==  msg.port:                             #line 410
        contents =  msg.datum.srepr ()                      #line 411
        f = open ( inst.filename, "w")                      #line 412
        if  f!= None:                                       #line 413
            f.write ( msg.datum.srepr ())                   #line 414
            f.close ()                                      #line 415
            send ( eh, "done",new_datum_bang (), msg)       #line 416
        else:                                               #line 417
            send_string ( eh, "✗", str( "open error on file ") +  inst.filename , msg)#line 418#line 419#line 420

class StringConcat_Instance_Data:
    def __init__ (self,):                                   #line 421
        self.buffer1 =  None                                #line 422
        self.buffer2 =  None                                #line 423
        self.scount =  0                                    #line 424#line 425
                                                            #line 426
def stringconcat_instantiate (reg,owner,name,template_data):#line 427
    name_with_id = gensymbol ( "stringconcat")              #line 428
    instp =  StringConcat_Instance_Data ()                  #line 429
    return make_leaf ( name_with_id, owner, instp, stringconcat_handler)#line 430#line 431#line 432

def stringconcat_handler (eh,msg):                          #line 433
    inst =  eh.instance_data                                #line 434
    if  "1" ==  msg.port:                                   #line 435
        inst.buffer1 = clone_string ( msg.datum.srepr ())   #line 436
        inst.scount =  inst.scount+ 1                       #line 437
        maybe_stringconcat ( eh, inst, msg)                 #line 438
    elif  "2" ==  msg.port:                                 #line 439
        inst.buffer2 = clone_string ( msg.datum.srepr ())   #line 440
        inst.scount =  inst.scount+ 1                       #line 441
        maybe_stringconcat ( eh, inst, msg)                 #line 442
    else:                                                   #line 443
        runtime_error ( str( "bad msg.port for stringconcat: ") +  msg.port )#line 444#line 445#line 446#line 447

def maybe_stringconcat (eh,inst,msg):                       #line 448
    if ( 0 == len ( inst.buffer1)) and ( 0 == len ( inst.buffer2)):#line 449
        runtime_error ( "something is wrong in stringconcat, both strings are 0 length")#line 450
    if  inst.scount >=  2:                                  #line 451
        concatenated_string =  ""                           #line 452
        if  0 == len ( inst.buffer1):                       #line 453
            concatenated_string =  inst.buffer2             #line 454
        elif  0 == len ( inst.buffer2):                     #line 455
            concatenated_string =  inst.buffer1             #line 456
        else:                                               #line 457
            concatenated_string =  inst.buffer1+ inst.buffer2#line 458
        send_string ( eh, "", concatenated_string, msg)     #line 459
        inst.buffer1 =  None                                #line 460
        inst.buffer2 =  None                                #line 461
        inst.scount =  0                                    #line 462#line 463#line 464

#                                                           #line 465#line 466
# this needs to be rewritten to use the low_level “shell_out“ component, this can be done solely as a diagram without using python code here#line 467
def shell_out_instantiate (reg,owner,name,template_data):   #line 468
    name_with_id = gensymbol ( "shell_out")                 #line 469
    cmd = shlex.split ( template_data)                      #line 470
    return make_leaf ( name_with_id, owner, cmd, shell_out_handler)#line 471#line 472#line 473

def shell_out_handler (eh,msg):                             #line 474
    cmd =  eh.instance_data                                 #line 475
    s =  msg.datum.srepr ()                                 #line 476
    ret =  None                                             #line 477
    rc =  None                                              #line 478
    stdout =  None                                          #line 479
    stderr =  None                                          #line 480

    ret = subprocess.run (  cmd,   input= s.encode('utf-8'), capture_output=True)
    rc = ret.returncode
    stdout = ret.stdout.decode('utf-8')
    stderr = ret.stderr.decode('utf-8')
                                                            #line 481
    if  rc!= 0:                                             #line 482
        send_string ( eh, "✗", stderr, msg)                 #line 483
    else:                                                   #line 484
        send_string ( eh, "", stdout, msg)                  #line 485#line 486#line 487#line 488

def string_constant_instantiate (reg,owner,name,template_data):#line 489
    global root_project                                     #line 490
    global root_0D                                          #line 491
    name_with_id = gensymbol ( "strconst")                  #line 492
    s =  template_data                                      #line 493
    if  root_project!= "":                                  #line 494
        s = re.sub ( "_00_",  root_project,  s)             #line 495#line 496
    if  root_0D!= "":                                       #line 497
        s = re.sub ( "_0D_",  root_0D,  s)                  #line 498#line 499
    return make_leaf ( name_with_id, owner, s, string_constant_handler)#line 500#line 501#line 502

def string_constant_handler (eh,msg):                       #line 503
    s =  eh.instance_data                                   #line 504
    send_string ( eh, "", s, msg)                           #line 505#line 506#line 507

def string_make_persistent (s):                             #line 508
    # this is here for non_GC languages like Odin, it is a no_op for GC languages like Python#line 509
    return  s                                               #line 510#line 511#line 512

def string_clone (s):                                       #line 513
    return  s                                               #line 514#line 515#line 516

# usage: app ${_00_} ${_0D_} arg main diagram_filename1 diagram_filename2 ...#line 517
# where ${_00_} is the root directory for the project       #line 518
# where ${_0D_} is the root directory for 0D (e.g. 0D/odin or 0D/python)#line 519#line 520
def initialize_component_palette (root_project,root_0D,diagram_source_files):#line 521
    reg = make_component_registry ()                        #line 522
    for diagram_source in  diagram_source_files:            #line 523
        all_containers_within_single_file = json2internal ( root_project, diagram_source)#line 524
        reg = generate_shell_components ( reg, all_containers_within_single_file)#line 525
        for container in  all_containers_within_single_file:#line 526
            register_component ( reg,mkTemplate ( container [ "name"], container, container_instantiator))#line 527#line 528#line 529
    initialize_stock_components ( reg)                      #line 530
    return  reg                                             #line 531#line 532#line 533

def print_error_maybe (main_container):                     #line 534
    error_port =  "✗"                                       #line 535
    err = fetch_first_output ( main_container, error_port)  #line 536
    if ( err!= None) and ( 0 < len (trimws ( err.srepr ()))):#line 537
        print ( "___ !!! ERRORS !!! ___")                   #line 538
        print_specific_output ( main_container, error_port) #line 539#line 540#line 541

# debugging helpers                                         #line 542#line 543
def nl ():                                                  #line 544
    print ( "")                                             #line 545#line 546#line 547

def dump_outputs (main_container):                          #line 548
    nl ()                                                   #line 549
    print ( "___ Outputs ___")                              #line 550
    print_output_list ( main_container)                     #line 551#line 552#line 553

def trimws (s):                                             #line 554
    # remove whitespace from front and back of string       #line 555
    return  s.strip ()                                      #line 556#line 557#line 558

def clone_string (s):                                       #line 559
    return  s                                               #line 560#line 561#line 562

load_errors =  False                                        #line 563
runtime_errors =  False                                     #line 564#line 565
def load_error (s):                                         #line 566
    global load_errors                                      #line 567
    print ( s)                                              #line 568
    print ()                                                #line 569
    load_errors =  True                                     #line 570#line 571#line 572

def runtime_error (s):                                      #line 573
    global runtime_errors                                   #line 574
    print ( s)                                              #line 575
    runtime_errors =  True                                  #line 576#line 577#line 578

def fakepipename_instantiate (reg,owner,name,template_data):#line 579
    instance_name = gensymbol ( "fakepipe")                 #line 580
    return make_leaf ( instance_name, owner, None, fakepipename_handler)#line 581#line 582#line 583

rand =  0                                                   #line 584#line 585
def fakepipename_handler (eh,msg):                          #line 586
    global rand                                             #line 587
    rand =  rand+ 1
    # not very random, but good enough _ 'rand' must be unique within a single run#line 588
    send_string ( eh, "", str( "/tmp/fakepipe") +  rand , msg)#line 589#line 590#line 591
                                                            #line 592
# all of the the built_in leaves are listed here            #line 593
# future: refactor this such that programmers can pick and choose which (lumps of) builtins are used in a specific project#line 594#line 595
def initialize_stock_components (reg):                      #line 596
    register_component ( reg,mkTemplate ( "1then2", None, deracer_instantiate))#line 597
    register_component ( reg,mkTemplate ( "?", None, probe_instantiate))#line 598
    register_component ( reg,mkTemplate ( "?A", None, probeA_instantiate))#line 599
    register_component ( reg,mkTemplate ( "?B", None, probeB_instantiate))#line 600
    register_component ( reg,mkTemplate ( "?C", None, probeC_instantiate))#line 601
    register_component ( reg,mkTemplate ( "trash", None, trash_instantiate))#line 602#line 603
    register_component ( reg,mkTemplate ( "Low Level Read Text File", None, low_level_read_text_file_instantiate))#line 604
    register_component ( reg,mkTemplate ( "Ensure String Datum", None, ensure_string_datum_instantiate))#line 605#line 606
    register_component ( reg,mkTemplate ( "syncfilewrite", None, syncfilewrite_instantiate))#line 607
    register_component ( reg,mkTemplate ( "stringconcat", None, stringconcat_instantiate))#line 608
    # for fakepipe                                          #line 609
    register_component ( reg,mkTemplate ( "fakepipename", None, fakepipename_instantiate))#line 610#line 611#line 612

def initialize ():                                          #line 613
    root_of_project =  sys.argv[ 1]                         #line 614
    root_of_0D =  sys.argv[ 2]                              #line 615
    arg =  sys.argv[ 3]                                     #line 616
    main_container_name =  sys.argv[ 4]                     #line 617
    diagram_names =  sys.argv[ 5:]                          #line 618
    palette = initialize_component_palette ( root_of_project, root_of_0D, diagram_names)#line 619
    return [ palette,[ root_of_project, root_of_0D, main_container_name, diagram_names, arg]]#line 620#line 621#line 622

def start (palette,env):
    start_helper ( palette, env, False)                     #line 623

def start_show_all (palette,env):
    start_helper ( palette, env, True)                      #line 624

def start_helper (palette,env,show_all_outputs):            #line 625
    root_of_project =  env [ 0]                             #line 626
    root_of_0D =  env [ 1]                                  #line 627
    main_container_name =  env [ 2]                         #line 628
    diagram_names =  env [ 3]                               #line 629
    arg =  env [ 4]                                         #line 630
    set_environment ( root_of_project, root_of_0D)          #line 631
    # get entrypoint container                              #line 632
    main_container = get_component_instance ( palette, main_container_name, None)#line 633
    if  None ==  main_container:                            #line 634
        load_error ( str( "Couldn't find container with page name /") +  str( main_container_name) +  str( "/ in files ") +  str(str ( diagram_names)) +  " (check tab names, or disable compression?)"    )#line 638#line 639
    if not  load_errors:                                    #line 640
        marg = new_datum_string ( arg)                      #line 641
        msg = make_message ( "", marg)                      #line 642
        inject ( main_container, msg)                       #line 643
        if  show_all_outputs:                               #line 644
            dump_outputs ( main_container)                  #line 645
        else:                                               #line 646
            print_error_maybe ( main_container)             #line 647
            outp = fetch_first_output ( main_container, "") #line 648
            if  None ==  outp:                              #line 649
                print ( "(no outputs)")                     #line 650
            else:                                           #line 651
                print_specific_output ( main_container, "") #line 652#line 653#line 654
        if  show_all_outputs:                               #line 655
            print ( "--- done ---")                         #line 656#line 657#line 658#line 659#line 660
                                                            #line 661#line 662
# utility functions                                         #line 663
def send_int (eh,port,i,causing_message):                   #line 664
    datum = new_datum_int ( i)                              #line 665
    send ( eh, port, datum, causing_message)                #line 666#line 667#line 668

def send_bang (eh,port,causing_message):                    #line 669
    datum = new_datum_bang ()                               #line 670
    send ( eh, port, datum, causing_message)                #line 671#line 672#line 673







count_counter =  0                                          #line 1
count_direction =  1                                        #line 2#line 3
def count_handler (eh,msg):                                 #line 4
    global count_counter, count_direction                   #line 5
    if  msg.port ==  "adv":                                 #line 6
        count_counter =  count_counter+ count_direction     #line 7
        send_int ( eh, "", count_counter, msg)              #line 8
    elif  msg.port ==  "rev":                               #line 9
        count_direction = - count_direction                 #line 10#line 11#line 12#line 13

def count_instantiator (reg,owner,name,template_data):      #line 14
    name_with_id = gensymbol ( "Count")                     #line 15
    return make_leaf ( name_with_id, owner, None, count_handler)#line 16#line 17#line 18

def count_install (reg):                                    #line 19
    register_component ( reg,mkTemplate ( "Count", None, count_instantiator))#line 20#line 21







def decode_install (reg):                                   #line 1
    register_component ( reg,mkTemplate ( "Decode", None, decode_instantiator))#line 2#line 3#line 4

decode_digits = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]#line 5
def decode_handler (eh,msg):                                #line 6
    global decode_digits                                    #line 7
    i = int ( msg.datum.srepr ())                           #line 8
    if  i >=  0 and  i <=  9:                               #line 9
        send_string ( eh, decode_digits [ i], decode_digits [ i], msg)#line 10#line 11
    send_bang ( eh, "done", msg)                            #line 12#line 13#line 14

def decode_instantiator (reg,owner,name,template_data):     #line 15
    name_with_id = gensymbol ( "Decode")                    #line 16
    return make_leaf ( name_with_id, owner, None, decode_handler)#line 17







def reverser_install (reg):                                 #line 1
    register_component ( reg,mkTemplate ( "Reverser", None, reverser_instantiator))#line 2#line 3#line 4

reverser_state =  "J"                                       #line 5#line 6
def reverser_handler (eh,msg):                              #line 7
    global reverser_state                                   #line 8
    if  reverser_state ==  "K":                             #line 9
        if  msg.port ==  "J":                               #line 10
            send_bang ( eh, "", msg)                        #line 11
            reverser_state =  "J"                           #line 12
        else:                                               #line 13
            pass                                            #line 14#line 15
    elif  reverser_state ==  "J":                           #line 16
        if  msg.port ==  "K":                               #line 17
            send_bang ( eh, "", msg)                        #line 18
            reverser_state =  "K"                           #line 19
        else:                                               #line 20
            pass                                            #line 21#line 22#line 23#line 24#line 25

def reverser_instantiator (reg,owner,name,template_data):   #line 26
    name_with_id = gensymbol ( "Reverser")                  #line 27
    return make_leaf ( name_with_id, owner, None, reverser_handler)#line 28#line 29







def delay_install (reg):                                    #line 1
    register_component ( reg,mkTemplate ( "Delay", None, delay_instantiator))#line 2#line 3#line 4

class Delay_Info:
    def __init__ (self,):                                   #line 5
        self.counter =  0                                   #line 6
        self.saved_message =  None                          #line 7#line 8
                                                            #line 9
def delay_instantiator (reg,owner,name,template_data):      #line 10
    name_with_id = gensymbol ( "delay")                     #line 11
    info =  Delay_Info ()                                   #line 12
    return make_leaf ( name_with_id, owner, info, delay_handler)#line 13#line 14#line 15

DELAYDELAY =  5000                                          #line 16#line 17
def first_time (m):                                         #line 18
    return not is_tick ( m)                                 #line 19#line 20#line 21

def delay_handler (eh,msg):                                 #line 22
    info =  eh.instance_data                                #line 23
    if first_time ( msg):                                   #line 24
        info.saved_message =  msg                           #line 25
        set_active ( eh)
        # tell engine to keep running this component with ;ticks' #line 26#line 27#line 28
    count =  info.counter                                   #line 29
    next =  count+ 1                                        #line 30
    if  info.counter >=  DELAYDELAY:                        #line 31
        set_idle ( eh)
        # tell engine that we're finally done               #line 32
        forward ( eh, "", info.saved_message)               #line 33
        next =  0                                           #line 34#line 35
    info.counter =  next                                    #line 36#line 37#line 38







def monitor_install (reg):                                  #line 1
    register_component ( reg,mkTemplate ( "@", None, monitor_instantiator))#line 2#line 3#line 4

def monitor_instantiator (reg,owner,name,template_data):    #line 5
    name_with_id = gensymbol ( "@")                         #line 6
    return make_leaf ( name_with_id, owner, None, monitor_handler)#line 7#line 8#line 9

def monitor_handler (eh,msg):                               #line 10
    s =  msg.datum.srepr ()                                 #line 11
    i = int ( s)                                            #line 12
    while  i >  0:                                          #line 13
        s =  str( " ") +  s                                 #line 14
        i =  i- 1                                           #line 15#line 16
    print ( s)                                              #line 17#line 18





