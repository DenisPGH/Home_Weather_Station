# Home_Weather_Station
Small project for showing temperature, barometric pressure and humidity. Video recording and store the result int db.
Video here: https://www.youtube.com/watch?v=nZmN1bYRu88 

1.	Hardware: 
1.1.	 Box with dimensions : 180x125x25mm
1.2.	Micro SD Card at least 8 GB
1.3.	HDMI Display 5 inch 700x480px
1.4.	Raspberry Pi 3 B
1.5.	Power supply at least 3A
1.6.	BME280 sensor (mine is 3.3V)
1.7.	Cables and Wires
1.8.	 Internet
1.9.	CSI Raspberry Pi Camera
1.10.	 I2C connection between Raspberry Pi and BME280:
connection	Raspberry Pi(pin number)	BME280
Clock	5	SCL
Data	3	SDA
+ 3.3V	1	VCC
GND	6	GND



2.	Installation of Raspberry Pi OS:
2.1.	 Download Windows Card Formatter and Format the SD Card(optional):
2.2.	 Download Raspberry Pi Imager from https://www.raspberrypi.com/software/ 
2.3.	Open the Imager and add the Image to the card.

3.	First boot on the Raspberry Pi and setup the machine:
3.1	Sudo apt-get update and upgrade
3.2	Activate the on screen keyboard with sudo apt install matchbox-keyboard or  sudo apt install onboard( if error with the bus : sudo apt-get install -y at-spi2-core)



4.	Setup the Raspberry Pi and the Application for work:
4.1.	 Check Python3  : python3
4.2.	 Install virtual environment on the raspberry pi : sudo   apt-get  install   python3-venv 
4.3.	 Install git : sudo apt install git
4.4.	Mkdir watch
4.5.	Cd watch
4.6.	Git clone git@github.com:DenisPGH/Home_Weather_Station.git
4.7.	Cd Home_Weather_Station
4.8.	 Install pip:     sudo apt install python3-pip
4.9.	Check pip: python3 -m pip –version
4.10.	Cd Wetter
4.11.	Create virtual environment IN the directory of the project:   python3 -m venv env
4.12.	Activate the environment: source env/bin/activate
4.13.	Check the environment: which python  (answer: .../env/bin/python )
4.14.	Install requirements.txt : python3 -m pip install -r requirements.txt
4.15.	To leave env :   deactivate
4.16.	Install all in Raspberry Pi system: python3 -m pip install -r requirements.txt
4.17.	Sudo reboot
4.18.	Sudo apt-get update
4.19.	Install VS Code :  sudo apt install code 
4.20.	Connect ssh via VSCode:
4.20.1.	Add ssh key to config file 
4.20.2.	‘Identity file: ~/.ssh/id_rsa’
4.21.	Give execute permission to main file in the project: sudo chmod 777 ~/main.py
4.22.	Error Tkinter:  pip install tk
4.23.	pip install RPi.bme280

5.	Configuration for running automatically the code:
5.1.	Create file:           sudo nano /usr/local/bin/wetter.sh        with content:
#! /bin/bash
export DISPLAY=:0
/usr/bin/python3 /home/raspi/Desktop/watch/Home_Weather_Station/Wetter/main.py

5.2.	 Give permission to execute the file sudo chmod 777  /usr/local/bin/wetter.sh    
5.3.	 Create file:        sudo nano /lib/systemd/system/wetter.service     with content: 
[Unit]
Description=Weather application
After=multi-user.target
After=graphical.target 
[Service]
ExecStart=/usr/local/bin/wetter.sh
Restart=always
StartLimitInterval=10
RestartSec=10
Restart=on-failure
User=<your_user> 
[Install]
WantedBy=multi-user.target
WantedBy=graphical.target


5.4.	Enable the service script to run after boot :  sudo systemctl enable wetter.service
5.5.	 Start the service :  sudo systemctl start wetter.service
5.6.	 Check if the service work well:  sudo systemctl status wetter.service
5.7.	 sudo systemctl daemon-reload
5.8.	sudo chmod 777 /lib/systemd/system/wetter.service
5.9.	(if error with import matplotlib) : sudo apt install python3-matplotlib
5.10.	(if error with import pandas)  : sudo apt install python3-pandas
5.11.	Follow the service live : journalctl -l -f -u wetter.service




6.	Setup the sensor:
6.1.	(if need) add user I2C in the /etc/group :   sudo adduser pi i2c
6.2.	 Install python i2c packages: sudo apt-get install i2c-tools python-pip
6.3.	 Detect which addresses has: i2cdetect -y 1       (1 or 0 channel) 
6.4.	Install bme280 library :         sudo pip install pimoroni-bme280 smbus 

7.	Video install:
7.1.	 # gst-launch-1.0 v4l2src device='/dev/video0'  ! "video/x-raw, format=RGB16, framerate=30/1, width=1920, height=1080" ! fpsdisplaysink video-sink=waylandsink text-overlay=false sync=false -v
7.2.	Install OpenCV: 
