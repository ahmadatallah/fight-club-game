from Tkinter import *
import time
            
class Test(Frame):
    
    def mouseDown(self, event):
        # remember where the mouse went down
        self.lastx = event.x
        self.lasty = event.y
        return(event.x,event.y)

    def mouseMove(self, event):
        # whatever the mouse is over gets tagged as CURRENT for free by tk.
        self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y
        
        
    def arrowMove(self,event):
         if event.keysym == 'Up':
             self.draw.move(1, 0, -3)
         elif event.keysym == 'Down':
             self.draw.move(1, 0, 3)
         elif event.keysym == 'Left':
             self.draw.move(1, -3, 0)
         elif event.keysym == 'Right':
             self.draw.move(1, 3, 0)



    def quit(self):
       self.draw.destroy()
       
    def mouseEnter(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="red")

    def mouseLeave(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="blue")


    #Grid 
    def checkered(self, canvas, line_distance):

         # vertical lines at an interval of "line_distance" pixel
         for x in range(line_distance,1000,line_distance):
                xp = canvas.create_line(x, 0, x, 1000, fill="#476042")

         # horizontal lines at an interval of "line_distance" pixel
         for y in range(line_distance,1000,line_distance):
                yp = canvas.create_line(0, y, 1000, y, fill="#476042")

   # def var_states(self):
   #     print("grid: %d" % (self.var1.get()))
   #     if(self.var1.get()):
   #         self.checkered(self.draw,20)
   #     else:
   #         pass
   #  def bulletRelease(self   
   #      while(1):
   #         if event.keysym == 'Up':
   #              for x in range(0, 60):
   #                self.draw.move(1, 4, 0)
   #                self.draw.update()
   #                time.sleep(0.05)

    def bulletRelease(self, canvas):   
        for x in range(0, 60):
            self.draw.move(1, 4, 0)
            self.draw.update()
            time.sleep(0.05)

            
    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT', activebackground='grey', activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',
                           command= self.quit)
        
        self.QUIT.pack(side=RIGHT)
        self.QUIT.config( height = 5, width = 10 )
        
        #for Grid
        
        #self.var1 = IntVar()
        #self.check1 = Checkbutton(self, text="Enable grid", variable= self.var1, command = self.var_states )
        #self.check1.pack(side=RIGHT)
        #self.tk = Tk()
        self.draw = Canvas(self, width=400, height=400)

        self.draw.pack(side=LEFT)
        bullet  = self.draw.create_oval( 30, 40 , 35, 45, fill = 'blue' )
        shooter = self.draw.create_polygon(10,50 , 50,50 , 50,40 , 45,25 , 15,25 , 10,40)
        self.draw.create_polygon(250,70 ,300,70 , 300,25 , 250,25)

        self.bulletRelease(bullet)
       
        #circ1 = self.draw.create_oval(100,100, 200,110,fill = 'blue')
        #circ2 = self.draw.create_oval(90,100, 100,110, fill = 'blue')
       
        self.draw.tag_bind(shooter, "<Any-Enter>", self.mouseEnter)
        self.draw.tag_bind(shooter, "<Any-Leave>", self.mouseLeave)  
        self.draw.tag_bind(shooter, "<KeyPress>", self.mouseEnter)
        Widget.bind(self.draw, "<Button-1>", self.mouseDown)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
        self.draw.bind_all('<KeyPress-Up>', self.arrowMove)
        self.draw.bind_all('<KeyPress-Down>', self.arrowMove)
        self.draw.bind_all('<KeyPress-Left>', self.arrowMove)
        self.draw.bind_all('<KeyPress-Right>', self.arrowMove)


       
    def __init__(self, master=None):

        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        


test = Test()
test.mainloop()
