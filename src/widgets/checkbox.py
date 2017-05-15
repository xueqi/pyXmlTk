'''
Created on May 11, 2017

@author: xueqi
'''
import Tkinter as _tk
class CheckBox(_tk.Checkbutton, object):
    '''
    classdocs
    '''


    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        self.value = _tk.IntVar()
        super(CheckBox, self).__init__(parent, variable = self.value, **kwargs)
    
    def setValue(self, value):
        if value:
            self.select()
        else:
            self.deselect()
    
    def getValue(self):
        return self.value.get() == 1