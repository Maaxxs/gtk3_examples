"""
There are 3 different ways to add handlers for the signals from elements in the
GUI (eg. the 'clicked' event, if a button is pressed). 

1. We define some functions and add them to a dictionary. The key is the name
    of the signal (as named in Glade) and the value the name of the function,
    which should be called.

2. We create a class. The methods must be called exactly as the signales were
    named in Glade. 

==> In both cases we call 'connect_signals()' and pass either the dictionary or
    the class as parameter. 

3. Of course, signals can be added manually. First, we get the object by its ID
    (named in Glade). 'get_object(ID)' will do that. Then we call the 
    'connect()' method. The first param is the signal name, the second one is 
    the function/method, which should be called.
    eg. window.connect('delete-event', Gtk.main_quit)

Both ways are working here. The default is, that the class Handler() is passed
to the 'connect_signals()' method. But you can pass the dictionary as well.
Try it! 
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# create a builder, load the file and get the main window by ID 'window1'
builder = Gtk.Builder()
builder.add_from_file("1connect.glade")
window = builder.get_object("window1")


# 1. way
def sayhello(buttonObject):
    print("Hey, I was added with a dict.")

def activate(button):
    print("Wohoo, you're hovering over the button.")

handlers = {
    "on_destroy": Gtk.main_quit,
    "on_button_clicked": sayhello,
    "on_button_hover": activate,
    }

# call the connect_signals() method and pass the dictionary handlers
#builder.connect_signals(handlers)



# 2. way
class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def on_button_clicked(self, button):
        print("I was added with a class.")
    
    def on_button_hover(self, button):
        print("Another event added with a class.")

# call the connect_signals() method and pass the class Handler()
builder.connect_signals(Handler())

# Show all elements of window and start the GTK main loop
window.show_all()
Gtk.main()
