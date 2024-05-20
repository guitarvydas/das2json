import py0d as zd

def main ():
    arg_array = zd.parse_command_line_args ()
    root_project = arg_array [0] 
    root_0D = arg_array [1]
    arg = arg_array [2]
    main_container_name = arg_array [3]
    diagram_names = arg_array [4]
    palette = zd.initialize_component_palette (root_project, root_0D, diagram_names, components_to_include_in_project)
    zd.run (palette, root_project, root_0D, arg, main_container_name, diagram_names, start_function,
              show_hierarchy=False, show_connections=False, show_traces=False, show_all_outputs=False)

def start_function (root_project, root_0D, arg, main_container):
    arg = zd.new_datum_string (arg)
    msg = zd.make_message("", arg)
    zd.inject (main_container, msg)

def components_to_include_in_project (root_project, root_0D, reg):
    zd.register_component (reg, zd.Template (name = "reader", instantiator = reader))
    zd.register_component (reg, zd.Template (name = "outputter", instantiator = outputter))

class FileDescriptor:
    def __init__ (self):
        self.filename = ""
        self.f = None
        self.atEof = True
        
def reader_handler (eh, msg):
    if msg.port == "filename":
        fname = msg.datum.srepr ()
        eh.instance_data.filename = fname
        try:
            f = open (fname, "r")
            eh.instance_data.f = f
        except:
            f = None
        if f != None:
            eh.instance_data.f = f
            eh.instance_data.atEof = False
        else:
            zd.send_string (eh, "✗", f"error opening file '{eh.instance_data.filename}'", msg)
    elif msg.port == "req":
        try:
            f = eh.instance_data.f
            if not eh.instance_data.atEof:
                c = f.read (1)
            else:
                c = ""
            if c == "":
                eh.instance_data.atEof = True
                zd.send_string (eh, "eof", True, msg)
            else:
                zd.send_string (eh, "", c, msg)
        except:
            zd.send_string (eh, "✗", f"error reading character from file '{eh.instance_data.filename}'", msg)
    else:
        zd.send_string (eh, "✗", f"unknown message to reader on port '{msg.port}'", msg)

def reader (reg, owner, name, template_data):
    name_with_id = zd.gensym ("reader")
    return zd.make_leaf (name_with_id, owner, FileDescriptor (), reader_handler)

import sys
def outputter_handler (eh, msg):
    if msg.port == "":
        print (msg.datum.srepr (), end='')
        zd.send_string (eh, "req", True, msg)
    elif msg.port == "eof":
        sys.exit (0)
    elif msg.port == "go":
        zd.send_string (eh, "req", True, msg)
    elif msg.port == "✗":
        print (f'*** {msg.datum.srepr ()}')
        sys.exit (1)
    else:
        # TODO: rewrite this to do something more useful
        print (f'unknown message to outputter on port "{msg.port}"')
        sys.exit (1)

def outputter (reg, owner, name, template_data):
    name_with_id = zd.gensym ("outputter")
    return zd.make_leaf (name_with_id, owner, None, outputter_handler)

main ()
