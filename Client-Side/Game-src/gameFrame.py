# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import random, string
from random import randint
import threading
import socket
import json
import pyaudio
import wave
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2
class alien(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.bind('<q>',quit)

        self.AvatarSpeed = 10
        self.score = 0
        self.bullets = []
        self.myHealth = 10
        self.initUI()
        self.bind_()
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(("",2700))  ##10.100.1.113##
        threading.Thread(target = self.socket_handle).start()

    '''def send_sound(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("*recording")
        frames = []
        for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
         data  = stream.read(CHUNK)
         frames.append(data)
         self.socket.sendall(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
    '''

    def initUI(self):
        self.parent.title("Fight Club Game")
        self.pack(fill=BOTH, expand=True)

#-----------frame one ------------#
        self.fram1= Frame(self, relief=RAISED,borderwidth=2)
        self.fram1.pack(fill=BOTH, side= LEFT, expand=True,padx=10,pady=10)

        self.canvas = Canvas(self.fram1,width=500)
        self.Avatar = self.canvas.create_oval(10, 10, 90, 90, outline='white', fill='blue', tags="myChip")
        # self.canvas.create_oval(50, 50, 100, 100, outline='white', fill='red', tags="m")
        self.canvas.pack(fill=BOTH,expand=True)
        self.drawObstacle(self.canvas,75,75,75,150,150,150,150,75)
        self.drawObstacle(self.canvas,300,150,375,150,375,75,300,75)
        self.drawObstacle(self.canvas,300,350,375,350,375,425,300,425)
        self.drawObstacle(self.canvas,150,350,75,350,75,425,150,425)

#-----------frame one ------------#

        #-----------frame Two ------------#
        fram2= Frame(self,relief=RAISED,borderwidth=1)
        fram2.pack(fill=BOTH,side=RIGHT,expand=False,padx=10,pady=10)
        lbl2 = Label(fram2, text="Chat History", width=20)
        lbl2.pack(side=TOP, padx=5, pady=5)
        self.chat_history = Text(fram2,width=40)
        self.chat_history.pack(fill=BOTH,expand=True)
        self.chat_history.config(state=DISABLED)
        self.chat_history.bind("<1>", lambda event: self.chat_history.focus_set())    #highlighting and copying
        self.chat_history.see(END)             # Scroll if necessary
#-----------frame Two ------------#

#-----------frame Three ------------#
        fram3= Frame(fram2)
        fram3.pack(fill=BOTH ,side=RIGHT,expand=True,padx=10,pady=10)

        self.message_entry = Entry(fram3)
        self.message_entry.pack(fill=X, expand=True)

        send_button= Button(fram3,text="Send",command=self.send)
        send_button.pack(side=BOTTOM,padx=5,expand=True)
#-----------frame Three ------------#

#-----------frame Four ------------#
        frame4= Frame(self)
        lbl4 = Label(frame4, text="Welcome: ", width=20)
        lbl4.pack(side=TOP, padx=5, pady=60)

        lbl3 = Label(frame4, text="Your Score: ", width=20)
        lbl3.pack(side=TOP, padx=5)
        self.myScore = Text(frame4,width=10,height=5,font=20)
        self.myScore.insert(INSERT, '10')
        self.myScore.config(state=DISABLED)
        self.myScore.pack(side=TOP,pady=30,expand=True)

        frame4.pack(fill=BOTH,side=BOTTOM,expand=True)
        send_button= Button(frame4,text="Say Something",command=self.recordAndSend,
                                width=30, height=3)
        send_button.pack(padx=5,expand=True)

        exit_button= Button(frame4,text="End Game!",command=self.endGame)
        exit_button.pack(side=BOTTOM,padx=5,expand=True, fill=X)

#-----------frame Four ------------#

    def updateScore(self):
        self.myScore.delete(0,END)
        self.myScore.config(state=NORMAL)
        self.myScore.insert(INSERT,self.myHealth)
        self.myScore.config(state=DISABLED)


    def recordAndSend(self):
        pass

    def endGame(self):
        # self.destroy()
        self.quit()
        # self.socket.shutdown(socket.SHUT_RDWR)
        '''
        close connection here
        '''

#-------------------------------------------------------------
    def drawObstacle(self,canvas,x1,y1,x2,y2,x3,y3,x4,y4):
        canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4)
        canvas.pack()
        canvas.update()

    def send(self):
        if len(self.message_entry.get()) != 0:
            current_msg= self.message_entry.get()
            # self.getMessge()
            player_name= self.getPlayerName()
            # player_message =self.getPlayerMessage()
            new_message= '<'+player_name +'> :' + current_msg + "\n"
            self.chat_history.config(state=NORMAL)
            self.chat_history.insert(INSERT,new_message)
            self.chat_history.config(state=DISABLED)
            curr_msg = self.serialize_message(current_msg)
            self.socket.send(curr_msg)
            # return current_msg
            '''
            current_msg: to be sent to the server/all player_message
            '''


    def getPlayerName(self):

        '''
        code to return player name
        to be displayed
        '''
        return 'player 1'

        # def getPlayerMessage(self):
        #     curr_msg = send()

        '''
        code to return player message
        to be displayed
        '''

    def randomword(self):
      return ''.join(random.choice(string.lowercase) for i in range(randint(3,9)))


    def motion(self,event):
        m = event.x
        n = event.y
        try:
            threading.Thread(target=self.bulletFire , args =(m,n)).start()
        except Exception, errtxt:
            print errtxt

    def socket_handle(self):
        while True:
             try:
                 json_data= self.socket.recv(1024)
                 if len(json_data) >0:
                    #   threading.Thread(target = self.readSocket, args =  json_data  ).start()
                    self.readSocket(json_data)
                    # time.sleep(0.025)
             except Exception as e:
                 raise



    def bulletFire(self,x,y):

        ##Connection Thread##
        # here You should take coordinates of avatar coordinates to draw the opposite player avatar_coords = (x1,y1,x2,y2)
        Avatar_coords  = self.canvas.coords("myChip")
        enemy_coords = self.canvas.coords("enemyAvatar")
        if len(enemy_coords) == 0:
            return

        limitx1 = enemy_coords[0]
        limitx2 = enemy_coords[2]
        limity1 = enemy_coords[1]
        limity2 = enemy_coords[3]

        diffX = x - Avatar_coords[0]
        diffY = y - Avatar_coords[1]

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

        normal = max( abs(bulletSpeed_X), abs(bulletSpeed_Y))

        bulletSpeed_X = (bulletSpeed_X/normal) * 10
        bulletSpeed_Y = (bulletSpeed_Y/normal) * 10
        json_map = self.serialize_bullet(bulletSpeed_X,bulletSpeed_Y)
        self.socket.send(json_map)
        tagname = self.randomword()
        bulletSize = 8
        bullet = self.canvas.create_oval(Avatar_coords[0], Avatar_coords[1], Avatar_coords[0] + bulletSize, Avatar_coords[1] + bulletSize, outline='white',fill='red',tags=tagname)
        self.canvas.pack()
        self.canvas.update()
        myHealth = 10
        while(True):
            time.sleep(0.025)

            #### connection thread ###
            #here you should send coordinates of the bullet in every time  bullet_coords = (x1,y1,x2,y2)
            bullet_coords = self.canvas.coords(tagname)

            stopx = bullet_coords[0]
            stopy = bullet_coords[1]

            self.canvas.move(bullet, bulletSpeed_X, bulletSpeed_Y)
            if ((75<stopy<150) or (350<stopy<425)):
                   if ((75 < stopx < 150) or (300 < stopx< 375) ):
                       self.canvas.delete(tagname)
                    #    addscored += 1
                       break
            if ((limity1<stopy<limity2)):
                   if ((limitx1 < stopx < limitx2)):
                       self.canvas.delete(tagname)
                       break
            self.canvas.update()

        # self.canvas.update()
        self.canvas.delete(tagname)

        self.canvas.update()
        self.canvas.delete(tagname)
        # self.score += addscored

        if (self.score == 10):
           self.canvas.delete("m")

    def moveDown(self,event):
        self.canvas.move(self.Avatar, 0, self.AvatarSpeed)
        self.canvas.update()
        Avatar_coords  = self.canvas.coords("myChip")
        json_map = self.serialize(Avatar_coords[0],Avatar_coords[1])
        self.socket.send(json_map)

    def moveUp(self,event):
        self.canvas.move(self.Avatar, 0, -self.AvatarSpeed)
        self.canvas.update()
        Avatar_coords  = self.canvas.coords("myChip")
        json_map = self.serialize(Avatar_coords[0],Avatar_coords[1])
        self.socket.send(json_map)

    def moveRight(self,event):
        self.canvas.move(self.Avatar, self.AvatarSpeed, 0 )
        self.canvas.update()
        Avatar_coords  = self.canvas.coords("myChip")
        json_map = self.serialize(Avatar_coords[0],Avatar_coords[1])
        self.socket.send(json_map)


    def moveLeft(self,event):
        self.canvas.move(self.Avatar, -self.AvatarSpeed, 0 )
        self.canvas.update()
        Avatar_coords  = self.canvas.coords("myChip")
        json_map = self.serialize(Avatar_coords[0],Avatar_coords[1])
        self.socket.send(json_map)

    def readSocket(self,data):
          try:
                data = json.loads(data)
                for key,value in data.items():
                        if key=="status":
                            if value==0:
                                self.canvas.delete("enemyAvatar")
                                break
                        elif key=="position":
                            self.addEnemy(value[0],value[1])
                        elif key=="bulletMove":
                            threading.Thread(target = self.enemyBullet , args=(value[0],value[1])).start()
                        elif key== "message":
                            new_message= '<'+'player_2' +'> :' + value + "\n"
                            self.chat_history.config(state=NORMAL)
                            self.chat_history.insert(INSERT,new_message)
                            self.chat_history.config(state=DISABLED)
          except Exception, errtxt:
                 print errtxt

    def serialize(self,pos_x,pos_y):
            json_map = {}
            position  = [pos_x,pos_y]
            json_map["position"] = position
            json_data = json.dumps(json_map)
            return json_data

    def serialize_message(self,message):
            json_map = {}
            json_map["message"] = message
            json_data = json.dumps(json_map)
            return json_data
    def serialize_bullet(self,pos_x,pos_y):
            json_map = {}
            position  = [pos_x,pos_y]
            json_map["bulletMove"] = position
            json_data = json.dumps(json_map)
            return json_data

    def serialize_finish(self):
           json_map = {}
           json_map["status"] = 0
           json_data = json.dumps(json_map)
           return json_data


    def enemyBullet(self,speedX,speedY):

            enemy_coords = self.canvas.coords("enemyAvatar")
            avatar_coords = self.canvas.coords("myChip")
            if len(enemy_coords)==0:
                return
            limitx1 = avatar_coords[0]
            limitx2 = avatar_coords[2]
            limity1 = avatar_coords[1]
            limity2 = avatar_coords[3]

            tagname = self.randomword()
            bulletSize = 8
            bullet = self.canvas.create_oval(enemy_coords[0], enemy_coords[1],enemy_coords[0] + bulletSize, enemy_coords[1] + bulletSize, outline='white',fill='red',tags=tagname)
            while (True):

                time.sleep(0.025)
                stop = self.canvas.coords(tagname)
                stopx = stop[0]
                stopy = stop[1]
                self.canvas.move(bullet, speedX, speedY)
                if ((75<stopy<150) or (350<stopy<425)):
                       if ((75 < stopx < 150) or (300 < stopx< 375) ):
                           self.canvas.delete(tagname)
                        #    addscored += 1
                           break

                if ((limity1<stopy<limity2)):
                       if ((limitx1 < stopx < limitx2)):
                           self.canvas.delete(tagname)
                           self.myHealth -= 1
                           self.updateScore()
                           if (self.myHealth == 0):
                               self.canvas.delete("myChip")
                            #    self.canvas.create_oval()
                               self.socket.send(self.serialize_finish())
                           break
                self.canvas.update()
            # self.canvas.update()
            self.canvas.delete(tagname)

    def addEnemy(self,x,y):
            self.canvas.delete("enemyAvatar")
            self.canvas.create_oval(x, y, x + 80, y + 80, outline='white',fill='black',tags="enemyAvatar")
            self.canvas.pack()
            self.canvas.update()

    def bind_(self):
        self.fram1.bind_all('<Button-1>',self.motion)
        self.fram1.bind_all("<Down>", self.moveDown)
        self.fram1.bind_all("<Up>", self.moveUp)
        self.fram1.bind_all("<Right>", self.moveRight)
        self.fram1.bind_all("<Left>", self.moveLeft)
        self.fram1.bind_all("<s>", self.moveDown)
        self.fram1.bind_all("<w>", self.moveUp)
        self.fram1.bind_all("<d>", self.moveRight)
        self.fram1.bind_all("<a>", self.moveLeft)



if __name__ == "__main__":
    root = Tk()
    app = alien(root)
    root.geometry("1000x800+300+100")
    root.minsize(width=1000 , height=600)   #****

    root.mainloop()
