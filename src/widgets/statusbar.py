'''
Created on May 10, 2017

@author: xueqi
'''
import Tkinter as _tk
class StatusBar(_tk.Frame, object):
    '''
    StatusBar for Application window
    '''

    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(StatusBar, self).__init__(parent, **kwargs)
        
        self.label = _tk.Label(self, bd = 1, relief = _tk.SUNKEN, anchor = _tk.W)
        self.label.pack(fill = _tk.X, expand = False)

    def set(self, strFormat, *args):
        self.label.config(text = strFormat % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

