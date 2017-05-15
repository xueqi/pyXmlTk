'''
Created on May 10, 2017

@author: xueqi
'''
import unittest
from widgets.xmlTk import XMLTkNode
import Tkinter as _tk


class TestXMLTkNode(unittest.TestCase):


    def setUp(self):
        self.xml_str = '''
            <Frame name = "parent" width = "200" height = "100">
                <Frame name = "child1">
                    <Meta> 
                        <pack>
                            <fill>Y</fill>
                            <expand>True</expand>
                        </pack>
                    </Meta>
                    <Label name = "label11" text = "label11text">
                        <Meta>
                            <grid>
                                <row>1</row>
                                <column>0</column>
                            </grid>
                        </Meta>
                    </Label> 
                    <Label name = "label12" text = "label12text" > 
                        <Meta>
                            <grid>
                                <row>0</row>
                                <column>1</column>                              
                            </grid>
                        </Meta>
                    </Label>
                </Frame>
                <Frame name = "child2">
                </Frame>
            </Frame>
        '''
        import xml.etree.ElementTree as ET
        self.xml_node = ET.fromstring(self.xml_str)

    def tearDown(self):
        pass

    @unittest.skip("haha")
    def testCreateWidget(self):
        from widgets.xmlTk import createWidget
        xml_str = '<Frame name="abc" width="100" height = "200" />'
        import xml.etree.ElementTree as ET
        root = ET.fromstring(xml_str)
        widget = createWidget(None, root.tag, root.attrib)
        print widget
        xml_str = '''
            <Frame name = "parent" width = "200" height = "100" >
                <Frame name = "child1">
                    <Label name = "label11" text = "label11text" /> 

                </Frame>
                <Frame name = "child2">
                </Frame>
            </Frame>
        '''
        root = ET.fromstring(xml_str)
        widget = createWidget(None, root.tag, root.attrib)
        children = widget.winfo_children()
        self.assertEqual(len(children), 0, "There should be 2 children, got %d" % len(children))
    @unittest.skip("haha")
    def testXMLTkNodeToWidget(self):
        node = XMLTkNode(self.xml_node)
        widget = node.toWidget(None)
        children = widget.winfo_children()
        self.assertEqual(len(children), 2, "There should be 2 children, got %d" % len(children))
        gchildren = widget.winfo_children()[0].winfo_children()
        self.assertEqual(len(gchildren), 2, "There should be 2 children, got %d" % len(gchildren))
    @unittest.skip("haha")
    def testGui(self):
        
        root = _tk.Tk()
        node = XMLTkNode.createFromXml(self.xml_str)
        node.toWidget(root)
        root.wm_title("ROOT TITLE")
        _tk.mainloop()
    
    def testCustomWidget(self):

        xml_str = '''<AppWindow name = "mainWindow" />
        '''
        node = XMLTkNode.createFromXml(xml_str)
        node.toWidget().mainloop()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()