from mainwindow import AppWindow
from lineedit import LineEdit
from checkbox import CheckBox
from numberWidget import FloatField, IntegerField
from filewidgets import FileInput, DirInput
from stextview import StreamTextView
from textview import TextView
from tabPanel import TabPanel


FileChooser = FileInput
DirChooser = DirInput

# tkinter

import Tkinter as _tk

Frame = _tk.Frame

Label = _tk.Label

from Tkinter import *

import tkMessageBox
showMessageBox = tkMessageBox.showinfo