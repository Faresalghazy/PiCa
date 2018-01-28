	

# *PiCa*

 is an open-source Raspberry pi car beginner's robotics project and a suitable introduction to IoT. While it is easy to replicate, the programming concepts used are of intermediate level(OOP and WebSockets)so understanding them may be difficult to beginners. On the other hand, PiCa is a fun way to get children into DIY and computers due to the easy to follow instructions made available here, while also having enough room for improvement for more adept programmers and makers (if you would like to contribute, please feel free to submit a pull request). PiCa is a 2 wheel Raspberry Pi based car, however, the Car class should be compatible with similar SoCs, such as Bannana Pi, Orange Pi, and ASUS Tinker Board.


----------


# Building the car
To make a car, you need the following:
 1. Car chassis
 2. DC motors
 3. Wheels
 4. A Raspberry Pi connected to the internet
 5. L298N Board

 If you have the parts lying around, feel free to use them, I used the following kit [found here](http://a.co/eoH4D1q) I would note that the motors are not of the best quality, but that is understandable at the price point.
After assembling the car chassis, mount the Pi and L298N on top. It is important to remember that the L298N should have a common ground from the Pi and battery pack, to do this, simply connect the Pi's GND pin(On a Raspberry pi 3 this could be pin number 39) to the battery pack GND wire (black) by twisting or soldering them together, then connect them to the L298N GND. Finally, the connections I made from the L298N to the wheels, and Pi to the L298N were as follows
![](https://github.com/Faresalghazy/PiCa/blob/master/pinout.png "pinout") , 











however you can use any GPIO pins you like.


----------


# Configuring the pi software
First, clone or download this repository as a .zip. Second, unpack it and note the location of the repository, we will assume it is on your home folder. In which case, open up a terminal and type the following:

    cd PiCa
    python3 Main.py
You should receive an output similar to :

    Socket now listening at port <number> 
Take note of this number as you will need it in the next step. If you would like to always use the same port feel free to change it in Main.py to one of your convenience (such as 34330).
For example, in Main.py you would change line number 20 to

    PORT = int(34330) 
You can find a suitable port using this Android application: [PortFinder](https://play.google.com/store/apps/details?id=com.centennialapps.portfinder&hl=en)

Lastly, you need to find the IP of your Pi, this can be done most easily through the terminal using the command:

    hostname -I
 You can expect an output of a number such as:
  XXX.XXX.X.XXX
This is your local IP adress, take note of it.
You are now ready to control your car :) .

## Configuring video
By default, video is disabled, uncomment the following line in Main.py using your favorite text editor to enable it:

    #thread.start_new_thread(sendvid, ())

By default, the framerate is 20 FPS and the port the video is transmitted over is 8000, to change this, change the previous line of code  (Currently line 40) to :

    thread.start_new_thread(sendvid, (<new framerate>,<new port>))

 For example, for an fps of 30 at port 8001:
    thread.start_new_thread(sendvid, (30,8001))

Finally, the default resolution is 320x180, if you would like to change it, edit the following line of code (Currently line 25):

        camera.resolution = (320, 180)
	
----------
# Controlling the car from your Android phone
	Possibly the simplest step, download the CarJoy developed by Centennial Apps from google play [here](https://play.google.com/store/apps/details?id=centennialapps.fares.carcontroller&hl=en). Enter the settings page, enter your IP and port  (note that this works with external IPs as well), make sure to press the set buttons. Go back and enjoy steering your car. Alternatively, you can use or develop any application that sends the steering angle as a UTF string to the car

	CarJoy is still under development,with the missing feature of having video built in, while this should be out soon, you can for now get a first person view of your car's camera using your favourite media player that supports online streams, make sure to reduce the buffer to as least at possible (in ideal world, you would set the buffer to zero, but try starting 300ms and experimenting to your convenv
----------

# Considerations and possible future updates

 - Currently, the Car.steer() method does not work with angles, but rather a small range, a future update could make the car move at exact angles rather than rotate right or left, and move forward and backward.
 - I am currently working on transmitting video from the Pi to the CarJoy app using UV4L and a Pi Cam module
 - PiCa is not *my* project, it is *our* project. I would be happy to see everyone contributing to it, as a result, if you are able to improve the Car class, please do so and submit a pull request, you will ofcourse be credited

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgyODIyMzgxN119
-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyODk0NTM5MV19
-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzNTcxODU0XX0=
-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwMTY3NjA5NV19
-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDY4MjI0MTddfQ==
-->