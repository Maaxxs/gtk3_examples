"""
Simple program to add two numbers.

Enter two numbers and press the '=' Button. If you entered numbers, then the 
text of the result label will be changed to the result. Otherwise you are 
asked to enter something valid.
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()

    def button_add(self, button):
        label_result = builder.get_object("label_result")
        num1 = builder.get_object("entry_number1").get_text()
        num2 = builder.get_object("entry_number2").get_text()
        try:
            label_result.set_text(str(int(num1) + int(num2)))
        except ValueError:
            label_result.set_text("Com'on... Enter sth valid...")



builder = Gtk.Builder()
builder.add_from_file("2add2Numbers.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
