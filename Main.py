'''
Main Driver program for PiCa, a Raspberry pi based car --- Get it? "Driver"
Responsible for starting video feed in thread, handling web socket communication and moving the car
Program by Fares Al Ghazy, started on the fifteenth of December 2017
'''

#Start with imports

from Car2 import Car
import socket
import subprocess
import picamera
import thread
import os

def sendvid(f=24,v=8160):
#Code to stream video to the interwebs using PiCam
#command from http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-camera/streaming-video-using-vlc-player
#Remove '-vf' if your video is upside down
    command= "raspivid -o - -t0 -hf -vf -w 640 -h 480 -n -fps "+f+"|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:"+v+"}' :demux=h264"
    os.system(command)
    


#start video feed in different thread
#uncomment to start video
#thread.start_new_thread(sendvid, ())
#Receive the angle from android app and steer the car

PORT = int(0)  # Port to communicate over, 0 will find any free port

HOST = '0.0.0.0' #listen from any device
pin1=38
pin2=40
pin3=36
pin4=32
myCar = Car(pin1,pin2,pin3,pin4)

#Global variables

serversocket = socket.socket()
serversocket.bind((HOST, PORT))

# Specify to only listen to one device
serversocket.listen(1)
print("Socket now listening at port " + str(serversocket.getsockname()[1]))
# Get and display input
print("n")
while True:
    # Find client socket

    connection, address = serversocket.accept()

    receivedstring = connection.recv(10).decode('utf-8')[2:]

    if (receivedstring == '-1'):
        print("shutdown")
        subprocess.Popen("sudo shutdown now", shell=True)

    print(receivedstring)
    
    myCar.steer(receivedstring)
    


