#!/usr/bin/python3

import os
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

battery_list: list = []

def get_battery_life():
    parameters = os.popen('upower -i /org/freedesktop/UPower/devices/battery_BAT0')
    output = parameters.read()
    battery_list.append(output.lstrip().strip().replace("\n", ''))
    return True

def on_activate(app):
    get_battery_life()
    win = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label=battery_list)
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    win.present()

app = Gtk.Application(application_id='org.flatpak.PythonApp')
app.connect('activate', on_activate)
app.run(None)
