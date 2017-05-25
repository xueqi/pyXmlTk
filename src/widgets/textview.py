'''
Created on May 12, 2017

@author: xueqi
'''
import Tkinter as _tk

class _TextView(_tk.Text, object):
    '''
    Add a scroll bar on textview
    '''

    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(TextView, self).__init__(parent, **kwargs)
    

class ScrollTextView(_tk.Frame, object):
    def __init__(self, parent, **kwargs):
        super(ScrollTextView, self).__init__(parent, **kwargs)
        
        self.hsbar = _tk.Scrollbar(self)
        self.vsbar = _tk.Scrollbar(self)
        self.vsbar.pack(side = _tk.RIGHT, fill = _tk.Y, expand = False)
        
        self.textview = _tk.Text(self, height = 10)
        self.textview.pack(fill = _tk.BOTH)
        
        self.hsbar.pack(side = _tk.BOTTOM, fill = _tk.X, expand = False)
        
        self.textview.config(yscrollcommand = self.vsbar.set)
        self.textview.config(xscrollcommand = self.hsbar.set)
    
    def see(self, *args, **kwargs):
        self.textview.see(*args, **kwargs)
    def insert(self, *args, **kwargs):
        self.textview.insert(*args, **kwargs)
TextView = ScrollTextView
    