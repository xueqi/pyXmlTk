'''
Created on May 12, 2017

@author: xueqi
'''
import Tkinter as _tk

class TextView(_tk.Text, object):
    '''
    classdocs
    '''

    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(TextView, self).__init__(parent, **kwargs)
    