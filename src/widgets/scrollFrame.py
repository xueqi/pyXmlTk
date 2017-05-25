'''
Created on May 15, 2017

@author: xueqi
'''

import Tkinter as _tk

class ScrollFrame(_tk.Frame, object):
    '''
    A scrollFrame, place in a canvas. Put the canvas as outer interface
    '''
    
    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        self.frame = _tk.Frame(parent, bg = 'black', **kwargs)
        self.canvas = _tk.Canvas(self.frame)
        self.vsbar = _tk.Scrollbar(self.frame, bg = '#123')
        self.hsbar = _tk.Scrollbar(self.frame, bg = '#567')
        
        super(ScrollFrame, self).__init__(self.frame, **kwargs)
        
        self.canvas.create_window((0,0), window = self, anchor = _tk.N + _tk.W)
        self.canvas.pack(side = _tk.LEFT, fill = _tk.BOTH, expand = True)
        self.vsbar.pack(fill = _tk.Y, side = _tk.RIGHT, expand = False)
        self.hsbar.pack(fill = _tk.X, side = _tk.BOTTOM, expand = False)
        self.canvas.config(scrollregion=self.canvas.bbox(_tk.ALL))
        self.canvas.config(xscrollcommand=self.hsbar.set)  
        self.vsbar.config(command=self.canvas.yview)      
        self.canvas.config(yscrollcommand=self.vsbar.set)
        self.hsbar.config(command=self.canvas.xview)      
    
    def update(self):
        self.canvas.config(scrollregion = [0,0,1000,1000])
        # self.canvas.config(scrollregion = self.canvas.bbox(_tk.ALL))
        super(ScrollFrame, self).update()
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def pack_forget(self):
        self.frame.pack_forget()
    
    def pack_info(self):
        return self.frame.pack_info()

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
    
    def destroy(self):
        frame = self.frame
        super(ScrollFrame, self).destroy()
        frame.destroy()