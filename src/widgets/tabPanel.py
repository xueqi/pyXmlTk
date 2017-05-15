'''
Created on May 12, 2017

@author: xueqi
'''

import Tkinter as _tk
import collections as _collections

import logging
logger = logging.getLogger(__name__)


class _Tab(object):
    def __init__(self, name, widget, title = None):
        if title is None: title = name
        self.name = name
        self.title = title
        self.widget = widget
        self.button = None
class TabPanel(_tk.Frame, object):
    '''
    classdocs
    '''
    
    def __init__(self, parent, **kwargs):
        '''
        Constructor
        '''
        super(TabPanel, self).__init__(parent, **kwargs)
        
        self._tabs = _collections.OrderedDict()
        self._currentIndex = -1
        # add tab area
        self.tabArea = _tk.Frame(self)
        self.tabArea.pack(side = _tk.TOP, fill = _tk.X, expand = False)
        
        
    def addTab(self, name, widget, title = None):
        if name in self._tabs:
            pass
        tab = _Tab(name, widget, title)
        btn = _tk.Button(self.tabArea, text = tab.title)
        btn.pack(side=_tk.LEFT, fill = _tk.NONE, expand = False)
        btn.bind("<Button-1>", self._switchTab)
        tab.button = btn
        self._tabs[name] = tab
    
    def _switchTab(self, event):
        ebtn = event.widget
        tabIdx = None
        # get the tab
        for idx, _tabName in enumerate(self._tabs.keys()):
            _tab = self._tabs[_tabName]
            if _tab.button == ebtn:
                tabIdx = idx
                break
        if tabIdx is not None:
            self.setCurrentTab(tabIdx)
        
    
    def removeTab(self, idx):
        if idx < 0 or idx >= len(self._tabs): 
            logger.warn("index out of range, idx: %s, len(tabs): %s" 
                        % (idx, len(self._tabs)))
            return
        tabToRemove = self._tabs[self._tabs.keys()[idx]]
        tabToRemove.button.destroy()
        tabToRemove.widget.pack_forget()
        if idx == self._currentIndex:
            self._currentIndex -=1
            self._showTab(self._currentIndex)
    @property
    def currentTab(self):
        if self._currentIndex < 0:
            if len(self._tabs) == 0: return None
            self._currentIndex  = 0
        
        return self._tabs[self._tabs.keys()[self._currentIndex]]
        
    def setCurrentTab(self, idx):
        '''Set current tab to the index idx
        '''
        if self._currentIndex == idx:
            return 
        if idx < 0 or idx >= len(self._tabs):
            return
        if self._currentIndex > 0 and self._currentIndex < len(self._tabs):
            self._hideTab(self._currentIndex)
        
        self._currentIndex = idx
        self._showTab(self._currentIndex)
    
    def _hideTab(self, idx):
        ''' Hide a tab. Do not bound check
        '''
        tab = self._tabs[self._tabs.keys()[idx]]
        tab.widget.pack_forget()
    
    def _showTab(self, idx):
        ''' show a tab. Do not bound check
        '''
        tab = self._tabs[self._tabs.keys()[idx]]
        tab.widget.pack(side=_tk.BOTTOM, fill=_tk.BOTH, expand = False) 