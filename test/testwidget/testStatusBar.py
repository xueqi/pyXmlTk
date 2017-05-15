'''
Created on May 10, 2017

@author: xueqi
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInit(self):
        from widgets.statusbar import StatusBar
        
        s = StatusBar(None)
        s.set("aa%s", 'b')
        self.assertEqual(s.label.cget("text"), "aab")
        s.clear()
        self.assertEqual(s.label.cget("text"), "")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()