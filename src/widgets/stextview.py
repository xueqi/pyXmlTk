''' Thread safe output stream console.
Created on May 12, 2017

@ref: http://effbot.org/zone/tkinter-threads.htm
@author: xueqi
'''
from .textview import TextView
import Tkinter as _tk
import Queue
_t = object()
class StreamTextView(TextView):
    '''
    classdocs
    '''

    def __init__(self, parent, **kwargs):
        '''
        '''
        super(StreamTextView, self).__init__(parent, **kwargs)
        # self.config(state=_tk.DISABLED)
        self.queue = Queue.Queue()
        self.update_me()

    def write(self, text):
        print "stextview: ", text
        self.queue.put(text)
    
    def clear(self):
        self.queue.put(_t)
    
    def update_me(self):
        
        try:
            while True:
                line = self.queue.get_nowait()
                if line is _t:
                    pass
                    #self.delete(1.0, _tk.END)
                else:
                    self.insert(_tk.END, str(line))
                self.see(_tk.END)
                self.update_idletasks()
        except Queue.Empty:
            pass
        
        self.after(100, self.update_me)