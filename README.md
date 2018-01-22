	

# *PiCa*

 is an open-source beginner's robotics project and a suitable introduction to IoT. While it is easy to replicate, the programming concepts used are of intermediate level(OOP and WebSockets)so understanding them may be difficult to beginners. On the other hand, PiCa is a fun way to get children into DIY and computers due to the easy to follow instructions made available here, while also having enough room for improvement for more adept programmers and makers (if you would like to contribute, please feel free to submit a pull request). PiCa is a 2 wheel Raspberry Pi based car, however, the Car class should be compatible with similar SoCs, such as Bannana Pi, Orange Pi, and ASUS Tinker Board.


----------


# Building the car.
To make a car, you need the following:
 1. Car chassis
 2. DC motors
 3. Wheels
 4. A Raspberry Pi connected to the internet
 5. L298N Board

 If you have the parts lying around, feel free to use them, I used the following kit: [http://a.co/eoH4D1q](http://a.co/eoH4D1q) I would note that the motors are not of the best quality, but that is understandable at the price point.
After assembling the car chassis, mount the Pi and L298N on top. It is important to remember that the L298N should have a common ground from the Pi and battery pack, to do this, simply connect the Pi's GND pin(On a Raspberry pi 3 this could be pin number 39) to the battery pack GND wire (black) by twisting or soldering them together, then connect them to the L298N GND. Finally, the connections I made from the L298N to the wheels, and Pi to the L298N were as follows:
(https://imgur.com/97e7FSS) , however you can use any GPIO pins you like.


----------


# Configuring the pi software
First, clone or download this repository as a .zip. Second, unpack it and note the location of the repository, we will assume it is on your home folder. In which case, open up a terminal and type the following

    ls PiCa
    python3 Main.py
You should receive an output similar to :

    Socket now listening at port AAAAAA 
Take note of 

You are now ready to control your car :) .


----------

# Controling the car from your Android phone

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ1MjkzNzA3Nl19
-->