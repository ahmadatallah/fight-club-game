# TCP-IPmultiplayerGame
#This Repo contains two sides one for clients (2 player maximum till now)
#Client-Side/Game-src/gameFrame.py
#and one for server  
#server.py

# Commands to test
#on server
# python Server-Side/Game-src/server.py <port number>
#on client
# python Client-Side/Game-src/gameFrame.py <port number>
#besides The IP number 

#server and client on the same
python Server-Side/Game-src/server.py <port number>
sleep 3
python Client-Side/Game-src/gameFrame.py <port number> &
python Client-Side/Game-src/gameFrame.py <port number>
