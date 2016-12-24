# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import random, string
from random import randint
import threading

class alien(object):


    def __init__(self):

        def quitButton(event):
            self.QUIT = Button(self.root, text='QUIT', activebackground='grey', activeforeground='#ffffff',
                               bg='#39c639',
                               highlightcolor='red', padx='5px', pady='10px',
                               command=quit)

            self.QUIT.pack(side="right", expand=True)
            self.QUIT.config(height=5, width=5)

        self.root = Tk()
            # self.m = 1
            # self.n = 1
        self.AvatarSpeed = 10
        self.score = 0
        self.bullets = []
        quitButton(self.root)
            # self.textMessage(self.root)
        self.canvas = Canvas(self.root, width=700, height=700)
        self.Avatar = self.canvas.create_oval(5, 5, 80, 80, outline='white', fill='blue', tags="myChip")
        self.canvas.create_oval(50, 50, 150, 150, outline='white', fill='blue', tags="m")
        self.canvas.pack()

        def randomword():
          return ''.join(random.choice(string.lowercase) for i in range(randint(3,9)))


        def motion(event):
            m = event.x
            n = event.y
            # print m, n
            try:
                threading.Thread(target=bulletFire , args =(m,n)).start()
            except Exception, errtxt:
                print errtxt




        def bulletFire(x,y):

            ##Connection Thread##
            # here You should take coordinates of avatar coordinates to draw the opposite player avatar_coords = (x1,y1,x2,y2)
            Avatar_coords  = self.canvas.coords("myChip")
            # print Avatar_coords

            diffX = x - Avatar_coords[0]
            diffY = y - Avatar_coords[1]

            #print diffX ,diffY

            if diffX==0 :
                bulletSpeed_X = 0
                bulletSpeed_Y = 1 * (diffY/abs(diffY))

            elif diffY==0 :
                bulletSpeed_Y = 0
                bulletSpeed_X = 1 * (diffX/abs(diffX))

            else:
                slope= diffY/diffX
                bulletSpeed_Y = abs(slope) * (diffY/abs(diffY))
                bulletSpeed_X = 1 * (diffX/abs(diffX))




            print bulletSpeed_X ,bulletSpeed_Y

            normal = max( abs(bulletSpeed_X), abs(bulletSpeed_Y))

            bulletSpeed_X = (bulletSpeed_X/normal) * 10
            bulletSpeed_Y = (bulletSpeed_Y/normal) * 10

            tagname = randomword()
            bulletSize = 8
            bullet = self.canvas.create_oval(Avatar_coords[0], Avatar_coords[1], Avatar_coords[0] + bulletSize, Avatar_coords[1] + bulletSize, outline='white',fill='red',tags=tagname)
            self.canvas.pack()
            self.canvas.update()

            addscored = 0
            while(True):


                time.sleep(0.025)

                #### connection thread ###
                #here you should send coordinates of the bullet in every time  bullet_coords = (x1,y1,x2,y2)
                bullet_coords = self.canvas.coords(tagname)
                stopx = bullet_coords[0]
                stopy = bullet_coords[1]
                # print  bullet_coords[1]
                # limity = bullet_coords[1]
                # limitx = bullet_coords[0]
                # tempy = limity
                # tempx = limitx
                # tempn = tempy
                # tempm = tempx
                # print tempn, tempm

                self.canvas.move(bullet, bulletSpeed_X, bulletSpeed_Y)
                if (stopy < 100):
                   if (50 < stopx < 150):
                      self.canvas.delete(tagname)
                      addscored += 1
                      break

            self.canvas.update()

            self.score += addscored

            if (self.score == 10):
               self.canvas.delete("m")

        def moveDown(event=None):
            self.canvas.move(self.Avatar, 0, self.AvatarSpeed)
            self.canvas.update()

        def moveUp(event=None):
            self.canvas.move(self.Avatar, 0, -self.AvatarSpeed)
            self.canvas.update()

        def moveRight(event=None):
            self.canvas.move(self.Avatar, self.AvatarSpeed, 0 )
            self.canvas.update()


        def moveLeft(event=None):
            self.canvas.move(self.Avatar, -self.AvatarSpeed, 0 )
            self.canvas.update()

        self.root.bind('<Button-1>', motion)
        self.root.bind("<Down>", moveDown)
        self.root.bind("<Up>", moveUp)
        self.root.bind("<Right>", moveRight)
        self.root.bind("<Left>", moveLeft)

        self.root.bind("<s>", moveDown)
        self.root.bind("<w>", moveUp)
        self.root.bind("<d>", moveRight)
        self.root.bind("<a>", moveLeft)
        self.root.mainloop()

if __name__ == "__main__":
     alientest = alien()
