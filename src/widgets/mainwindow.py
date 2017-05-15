import Tkinter as _tk
import logging

from .statusbar import StatusBar


logger = logging.getLogger(__name__)
class AppWindow(_tk.Toplevel, object):
    def __init__(self, parent, isMasterWindow = True, **kwargs):
        width = kwargs.pop("width", 400)
        height = kwargs.pop("height", 300)
        super(AppWindow, self).__init__(parent, width = width, height = height, bg = "yellow", **kwargs)
        self.parent = parent
        if parent:
            parent.update()
            parent.minsize(parent.winfo_width(), parent.winfo_height())
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.showCloseMessage = False
        self.statusBar = None
        self.buildWindow()
        self.isMasterWindow = isMasterWindow

    def buildWindow(self):
        self.buildMenu()
        self.buildStatusBar()
        self.buildBarButton()
        frame = _tk.Frame(self, bg = "black")
        frame.grid(row=1, column = 0, stick = _tk.S + _tk.N + _tk.W + _tk.E)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.buildMainWindow(frame)
        self.statusBar.set("Done build window")

    def buildMenu(self):
        pass
    
    def pack(self, *args, **kwargs):
        '''    App window does not has pack option
        '''
        logger.warn("No pack function for AppWindow")

    def buildStatusBar(self):
        ''' Create a default status bar
        '''
        self.statusBar = StatusBar(self, bg="red")
        self.statusBar.grid(row=2, sticky = _tk.W + _tk.E)
    def buildBarButton(self):
        pass

    
    def buildMainWindow(self, parent = None):
        ''' Build main window area. 
            override this method
        '''
#        frame = _tk.Frame(self, width = 400, height = 300)
#        frame.pack(fill = _tk.BOTH, side=_tk.BOTTOM)
        raise Exception("This should be overrided")
        pass
    
    def close(self):
        import tkMessageBox
        if self.showCloseMessage:
            if not tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
                return
        if self.isMasterWindow and self.parent:
            self.parent.destroy()
        else:
            self.destroy()
        
