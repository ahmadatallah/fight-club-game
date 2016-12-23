# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import random, string
from random import randint
import threading

class alien(object):
     def __init__(self):
        self.root = Tk()

        self.m=1
        self.n=1

        self.bullets = []

        self.canvas = Canvas(self.root, width=400, height = 400)
        self.canvas.pack()
        self.root.after(0, self.animation)


        def randomword():
          return ''.join(random.choice(string.lowercase) for i in range(randint(5,25)))


        def motion(event):
            self.m=event.x
            self.n = event.y
            #print('{}, {}'.format(self.m,self.n))


        def bulletFire():

            tagname = randomword()

            bulletSpeed = 10
            bulletSize = 8


            bullet = self.canvas.create_oval(self.m, self.n, self.m + bulletSize, self.n + bulletSize, outline='white',fill='red',tags=tagname)
            self.canvas.pack()
            self.canvas.update()

            for i in range(0,50):

                time.sleep(0.025)
                self.canvas.move(bullet, 0, -bulletSpeed)
                self.canvas.update()

            self.canvas.delete(tagname)



        def draw(event=None):

           print "space"
           t1 = threading.Thread(target=bulletFire)
           t1.start()

        draw()



        self.root.bind('<Motion>', motion)
        self.root.bind("<space>", draw)
        self.root.mainloop()


     def animation(self):

        while True:

            self.canvas.delete("myChip")
            myChip = self.canvas.create_oval(self.m, self.n, self.m + 80, self.n + 80, outline='white',fill='blue',tags="myChip")
            self.canvas.pack()
            self.canvas.update()


alien()
