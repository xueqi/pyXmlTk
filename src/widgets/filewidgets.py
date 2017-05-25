'''
Created on May 11, 2017

@author: xueqi
'''
import Tkinter as _tk
from widgets.lineedit import LineEdit

class FileInput(_tk.Frame, object):
    '''
    classdocs
    '''
    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(FileInput, self).__init__(parent, **kwargs)
        
        self.txt = LineEdit(self)
        self.txt.pack(side = _tk.LEFT, fill = _tk.X, expand = True)
        self.txt.bind("<FocusOut>", self.focusOut)
        
        self.btn = _tk.Button(self, text = "Browse")
        
        self.btn.pack(side=_tk.RIGHT, expand=False)
        self.btn.bind("<Button-1>", self.selectFile)
        self.filetypes = []
        self.initialdir = None
    
    def focusOut(self, event = None):
        self.txt.xview(len(self.txt.getValue()) - 1)
    
    def selectFile(self, event = None):        
        # open a box to select file
        
        import tkFileDialog
        import os
        options = {}
        if self.initialdir is not None and os.path.exists(self.initialdir):
            options['initialdir'] = self.initialdir
        
        if len(self.filetypes) != 0:
            options["filetypes"] = self.filetypes
        
        filename = tkFileDialog.askopenfilename(**options)
        self.setValue(filename)
    
    def getValue(self):
        return self.txt.getValue()
    
    def setValue(self, value):
        self.txt.setValue(value)
        self.focusOut()

class DirInput(FileInput):
    def __init__(self, parent, **kwargs):
        super(DirInput, self).__init__(parent, **kwargs)
    
    def selectFile(self, event):
        import tkFileDialog
        import os
        options = {}
        if self.initialdir is not None and os.path.exists(self.initialdir):
            options['initialdir'] = self.initialdir
        dirname = tkFileDialog.askdirectory(**options)
        self.setValue(dirname)
        