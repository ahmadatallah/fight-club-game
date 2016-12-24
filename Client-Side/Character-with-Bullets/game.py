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

        self.AvatarSpeed = 10;

        self.bullets = []

        self.canvas = Canvas(self.root, width=700, height = 700)
        self.canvas.pack()
        self.Avatar = self.canvas.create_oval(5, 5, 80, 80, outline='white',fill='blue',tags="myChip")
        self.canvas.pack()


        def randomword():
          return ''.join(random.choice(string.lowercase) for i in range(randint(3,9)))


        def motion(event):
            m= event.x
            n = event.y

            t1 = threading.Thread(target=bulletFire , args =(m,n))
            t1.start()
            #print('{}, {}'.format(m,n))


        def bulletFire(x,y):

            Avatar_coords  = self.canvas.coords("myChip")

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

            for i in range(0,50):

                time.sleep(0.025)
                self.canvas.move(bullet, bulletSpeed_X, bulletSpeed_Y)
                self.canvas.update()

            self.canvas.delete(tagname)




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




alien()
