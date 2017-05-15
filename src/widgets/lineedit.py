'''
Created on May 11, 2017

@author: xueqi
'''
import Tkinter as _tk

class LineEdit(_tk.Entry, object):
    '''
        line edit
    '''
    
    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(LineEdit, self).__init__(parent, kwargs)
    
    def getValue(self):
        return self.get()

    def setValue(self, value):
        self.insert(0, "%s" % value)