'''
Created on May 11, 2017

@author: xueqi
'''

import Tkinter as _tk
class NumberField(_tk.Entry, object):
    '''
    classdocs
    '''

    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(NumberField, self).__init__(parent, **kwargs)
        self.__value = ""
        self.__variable = _tk.StringVar()
        self.__variable.trace("w", self.__callback)
        self.config(textvariable = self.__variable)
        self.typeClass = str
    
    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(newvalue)
        else:
            self.__value = value
    
    def validate(self, value):
        if self.get() in ['+', '-']: return value
        try:
            if value:
                v = self.typeClass(value)
                return "%s" % v
            return value
        except ValueError:
            return None
    
    
    def getValue(self):
        return self.typeClass(self.get())
    
    def setValue(self, value):
        self.insert(0, "%s" % value)
    
class FloatField(NumberField):
    def __init__(self, parent, **kwargs):
        super(FloatField, self).__init__(parent, **kwargs)
        self.typeClass = float
    
    def validate(self, value):
        if value in ['+.', '-.']: return value
        return super(FloatField, self).validate(value)

class IntegerField(NumberField):

    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(IntegerField, self).__init__(parent, **kwargs)
        self.typeClass = int
    
        