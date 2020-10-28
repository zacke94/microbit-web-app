# Microbit Web application 

### **This is a Windows 10 product for monitoring temperatures/light-levels of up to two Microbit's in the same room.**
</br> 

**Features:**
* web application where you can see the readings in realtime.
* show highest temperatures and lowest light-levels ever recorder, including time and date.
* Choose visual location where your Microbit's are located in your room.
* "Start readings.exe" application to start the reading of your Microbit's, up to two Microbit's.

</br>**How to install the and run the web application:**
1. Download and install Python 3.9.0 for Windows: https://www.python.org/downloads/
	* make sure you choose "Add Python 3.9 to PATH".
2. Open the "Command Promt" in Windows by press Windows+R buttons and search for "cmd".
3. Type ```pip --version``` to see that Python installed the path of Python correctly
	* if ```pip``` could not be found, please do step 4.
4. Add Python to PATH manually. (Skip to step 5 if ```pip``` was found)
	1. press Windows+R buttons and search for ```sysdm.cpl```
	2. Go to "Advanced" and click "Environment Variables"
	3. In "System variable", choose "Path" and click "Edit".
	4. Click "New", paste your Python 3 installation folder path and click "OK".
		* most common path is: ```C:\Users\<user>\AppData\Local\Programs\Python\Python39```
		* type ```pip --version``` in the "Command Promt" again to check if pip was found.
5. Open "Command Promt" and to go where your "microbit-web-app-main" folder is by typing ```cd```.
	* for example, if you open "Command Promt" your current location should be ```C:\Users\<user>``` 
	* You can navigate by going foward using ```cd <folder>```, or go back one step by with ```cd ..```
6. Once you're in the correct folder, type ```python -m  venv venv``` to create a virtual environment. Activate your virtual environment by typing ```venv\Scripts\activate``` and press enter.
7. Type ```pip install -r requirements.txt``` and press enter to install necessary packages for your web application in your virtual environment. 
8. Type ```flask run``` to start your web application, you can access it in your web browser at ```http://127.0.0.1:5000/```. To stop the web application, press Ctrl+C in the "Command Promt".

</br>**How to install your Microbit's:**
1. Plug in one of your Microbit's to your computer via USB that is going to be your "master".
2. From the folder "hex_files", drag the "microbit_master.hex" file into the Microbit device that should pop up after you have plugged in your Microbit. Now your Microbit is flashed and ready to use, and this Microbit is the one that is required to be connected via USB all the time you want to run your Microbit(s), no matter what if you are going to use one or two Microbit's. ***This step you only have to do once.**
3. If you want to use a second Microbit (slave), plug in that specific Micobit via USB to your computer and drag the "microbit_slave.hex" file into the device that should have popped up. Once done, remove the device from the computer. ***Note that you don't have to have the second Microbit connected to be able run the first Microbit.** 

</br>**How to run your Microbit's:**
1. Plug in your first (master) Microbit via USB to your computer
	* if you want to use your second (slave) Masterbit, connect it to a battery.
2. Launch "Start readings.exe", it can take up to 5-10 seconds.
	* if Windows try to stop you from open the application due to safety reason, click on "More infomation", and then "Run anyway"
3. Click "Start reading" to start your Microbit(s).
	* The Microbit connected to the USB-port should now be  blink every second.
4. Click "Stop reading" to stop your Microbit's. The window will automatic close in 5 seconds. **Do not close the window manually after clicked "Stop reading", because it's doing necessary work in the background.**

