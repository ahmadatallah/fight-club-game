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
        self.score = 0
        self.m=1
        self.n=1
        self.bullets = []
        self.canvas = Canvas(self.root, width=800, height = 800)
        ## this should sent form the player but here is fixed for
        ## just for test
        self.canvas.create_oval(50, 50, 150, 150, outline='white',fill='blue',tags="m")
        self.canvas.pack()
        self.root.after(0, self.animation)


        def randomword():
          return ''.join(random.choice(string.lowercase) for i in range(randint(5,25)))


        def motion(event):
            self.m =  event.x
            self.n = event.y
            # print('{}, {}'.format(self.m,self.n))


        def bulletFire():

            tagname = randomword()

            bulletSpeed = 10
            bulletSize = 20

            bullet = self.canvas.create_oval(self.m, self.n, self.m + bulletSize, self.n + bulletSize, outline='white',fill='red',tags=tagname)
            self.canvas.pack()
            self.canvas.update()
            tempn = self.n
            tempm = self.m
            addscored = 0
            while(True):

                time.sleep(0.025)
                limity = tempn - bulletSpeed
                temp  = limity
                tempn = temp
                self.canvas.move(bullet, 0, -bulletSpeed)
                if (tempn < 100 ):
                    if (50 < tempm < 150):
                       self.canvas.delete(tagname)
                       addscored += 1
                       break
                       # print tempn
                # print tempn

            self.canvas.update()
            self.score += addscored
            print self.score
            if (self.score == 10 ):
                 self.canvas.delete("m")



        def draw(event):
           print "space"
           t1 = threading.Thread(target=bulletFire)
           t1.start()




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
