import xml.etree.ElementTree as _ET
import Tkinter as _tk
import collections as _collections


import widgets as _widgets

class XMLTkNode(object):
    def __init__(self, node, parent = None):
        self.node = node
        self.parent = parent
        self.layout = None # grid or pack. In Tk, this depends on the children 
        self.widget = None # the widget that represent current node
        
    def toWidget(self, parent = None):
        self.widget = createWidget(parent, self.node.tag, self.node.attrib)
        if parent is not None:
            self.pack(self.widget)
        for node in self.node:
            if node.tag in ['Meta']: continue
            w = XMLTkNode(node, self)
            w.toWidget(self.widget)
        return self.widget
    
    def getLayoutMeta(self):
        ''' get Layout info from meta
        '''
        meta = self.node.find('Meta')

        layouts = _collections.OrderedDict()
    
        if meta is not None:
            for lostr in ['grid', 'pack', 'place']:

                lo = meta.find(lostr)
                if lo is not None:
                    
                    layouts[lostr] = {}
                    for child in lo:
                        layouts[lostr][child.tag] = getValue(child.text)

        return layouts
        
    
    def pack(self, widget):
        '''
            layout the widget using layout managers. 
            If parent layout is not determined, use the layout specified
            
            @param widget: The widget to pack.
        '''
        # check the parent packing option
        pLayout = None
        if self.parent:
            pLayout = self.parent.layout
        layouts = self.getLayoutMeta()
        
        if len(layouts) == 0: 
            widget.pack()
            return
        
        if pLayout is None or pLayout in layouts:
            if pLayout is None:
                pLayout = layouts.keys()[0]
            if hasattr(widget, pLayout):
                tLayout = layouts[pLayout]
                layoutFunc = getattr(widget, pLayout)
                layoutFunc(**layouts[pLayout])
            if self.parent:
                self.parent.layout = pLayout
        else:
            raise Exception("Conflict layout: \nparent: %s, self: %s" 
                  % (pLayout, str(layouts.keys())))
            
    @staticmethod
    def createFromXmlFile(filename):
        doc = _ET.parse(filename)
        node = doc.getroot()
        return XMLTkNode(node)
    
    @staticmethod
    def createFromXml(xml_str):
        node = _ET.fromstring(xml_str)
        return XMLTkNode(node)
    
def getValue(s):
    '''
        get the true value from s
    '''
    if s == "True": return True
    if s == "False": return False
    if s.startswith("tk."):
        value = s[3:]
        if hasattr(_tk, value):
            value = getattr(_tk, value)
            return value
    return s
    
def createWidget(parent, tag, attrib):

    if hasattr(_tk, tag):
        widgetClass = getattr(_tk, tag)
    elif hasattr(_widgets, tag):
        widgetClass = getattr(_widgets, tag)
    
    else:
        widgetClass = _tk.Frame
    
    for key in attrib:
        attrib[key] = getValue(attrib[key])
        
    print attrib
    widget = widgetClass(parent, **attrib)
    return widget

if __name__ == "__main__":
    pass
