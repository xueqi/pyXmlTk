'''
Created on May 16, 2017

@author: xueqi
'''

def main():
    import widgets as _w
    
    r = _w.Tk()
    f = _w.ScrollFrame(r)
    f.pack(side = _w.TOP, fill = _w.BOTH, expand = True)
    for i in range(20):
        lbl1 = _w.Label(f, text = 'label%s' % i)
        lbl1.pack()
    f.update()
    r.mainloop()

if __name__ == '__main__':
    main()