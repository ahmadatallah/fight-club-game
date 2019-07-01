#!/bin/bash
python Server-Side/Game-src/server.py 3300
sleep 3
python Client-Side/Game-src/gameFrame.py 3300  &
python Client-Side/Game-src/gameFrame.py 3300

