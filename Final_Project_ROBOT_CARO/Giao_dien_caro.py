from tkinter import *
import cx_Freeze
import random
import sys

class giaodien_1 :
    def __init__(self,master_1) :
        self.master = master_1
        self.select = Label(self.master,text= 'Chọn chế độ chơi:))', font = ('arial', 20))
        self.select.grid(row= 0, column= 0, padx= 50,sticky= 'w', pady=20)
        self.select.place(x= 50,y=50)
        self._3x3 = Button(self.master,bg= 'red',fg= 'snow',text= '3x3', font = ('arial', 30), command= self.mode_3x3 )
        self._3x3.place(x= 100,y=100)
        self._5x5 = Button(self.master,bg= 'blue',fg= 'snow',text= '5x5', font = ('arial', 30), command= self.mode_5x5 )
        self._5x5.place(x= 200,y=100)
        self._7x7 = Button(self.master,bg= 'green',fg= 'snow',text= '7x7', font = ('arial', 30), command= self.mode_7x7 )
        self._7x7.place(x= 300,y=100)

        self.test1 = Button(self.master,bg= 'black',fg= 'snow',text= 'TEST1', font = ('arial', 15), command= self.testsan1 )
        self.test1.place(x= 100,y=300)
        self.test2 = Button(self.master,bg= 'black',fg= 'snow',text= 'TEST2', font = ('arial', 15), command= self.testsan2 )
        self.test2.place(x= 200,y=300)
        self.test3 = Button(self.master,bg= 'black',fg= 'snow',text= 'TEST3', font = ('arial', 15), command= self.testsan3 )
        self.test3.place(x= 300,y=300)

        self.stop = Button(self.master,bg= 'red',fg= 'snow',text= 'STOP', font = ('arial', 20), command= self.exit )
        self.stop.place(x= 200,y=200)
        
    def mode_3x3(self) :  
        
        import x3
        x3.version_3x3()

    def mode_5x5(self) :  
        
        import x5
        x5.version_5x5()
        
    def mode_7x7(self) :  
        
        import x7
        x7.version_7x7()

    def testsan1(self) :
        import x3
        x3.test_san1()
    
    def testsan3(self) :
        import x7
        x7.TEST()
    
    def testsan2(self) :
        import x5
        x5.test_san2()



    def exit(self):
        quit()
    

def main() :
    ROBOT = Tk()
    ROBOT.title('ROBOT CARO')
    ROBOT.geometry('500x350+1080+0')
    ROBOT.resizable(True,True)
    app = giaodien_1(ROBOT)
    ROBOT.mainloop()

if __name__ == '__main__' :
    main()