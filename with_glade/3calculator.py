"""
Simple and small calculator with limited capabilities.

You can use one operator (+, -, *, /) multiple times per calculation, but you 
cannot use multiple operators in one calculation.
"""


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def __init__(self):
        self.textfield = builder.get_object("entry_field")
        self.execute = {
            "+": self.add,
            "-": self.sub,
            "/": self.div,
            "*": self.mul,
        }
        self.errorMsg = "Only numbers allowed and only one operator per \
calculation allowed." 

    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def btn_clear(self, btton):
        self.textfield.set_text("")

    def btn_clicked(self, button):
        """ Add the label of the pressed button to the text of 'textfield'. """
        value = button.get_label()
        text = self.textfield.get_text()
        self.textfield.set_text(text + value)

    def btn_result(self, button):
        """ Parse the text of 'textfield' and call methods accordingly. """
        text = self.textfield.get_text()
        for operation in "+-/*":
            splitted = text.split(operation)
            if len(splitted) > 1:
                for i in splitted:
                    if not self.is_numeric(i):
                        self.textfield.set_text("")
                        print(splitted)
                        raise ValueError(self.errorMsg)
                self.execute[operation](splitted)
    
    def is_numeric(self, number):
        """ Check, if given string can be converted to a number.
            Since there is no builtin function, we have to do it on our own.
            This is the recommended way to do it. """
        try:
            float(number)
        except ValueError:
            return False
        return True

    def add(self, vars):
        """ Add all numbers of list 'vars'. """
        result = 0
        for i in vars:
            result += float(i)
        self.textfield.set_text(str(result))
    
    def sub(self, vars):
        """ Substract all numbers from the first number of list 'vars'. """
        result = float(vars[0])
        for i in vars[1:]:
            result -= float(i)
        self.textfield.set_text(str(result))

    def mul(self, vars):
        """ Multiply alle numbers of list 'vars'. """
        result = float(vars[0])
        for i in vars[1:]:
            result *= float(i)
        self.textfield.set_text(str(result))

    def div(self, vars):
        """ Divide the first number through all following numbers of list 'vars'."""
        result = float(vars[0])
        for i in vars[1:]:
            result /= float(i)
        self.textfield.set_text(str(result))



builder = Gtk.Builder()
builder.add_from_file("3calculator.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
