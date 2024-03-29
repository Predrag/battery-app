#!/usr/bin/python3


import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os


class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Hello World")
        self.get_battery_life()

        self.button = Gtk.Button(label=str(self.get_battery_life()))
        self.button.connect("clicked", lambda x: self.close())
        self.add(self.button)

    def get_battery_life(self):
        parameters = os.popen('upower -i /org/freedesktop/UPower/devices/battery_BAT0')
        output = parameters.read()
        return output.lstrip().strip().replace("\n", '')

    def on_button_clicked(self, widget):
        print("Hello World")


if __name__ == '__main__':
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

