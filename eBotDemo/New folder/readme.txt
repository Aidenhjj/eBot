SUTD
2D Design Challenge
Term 3, 2013
Most recent update:  19-Feb-2013

INTRODUCTION
------------

This readme file explains the necessary software and documentations
to complete the 2D design project .


SOFTWARE
--------

To do this 2D design you will need the following softwares:
* Python 2.7 : http://epd-free.enthought.com/?Download=Download+EPD+Free+7.3-2 
* Digital World Library : http://tiny.cc/libdw 
* Driver USB to serial: http://www.ftdichip.com/Drivers/VCP.htm

For Windows:
* 7-Zip : Packing/ unpacking tar and GZip files: http://www.7-zip.org

INSTALLATION
------------

This section assumes that you have Python 2.7 already installed. 

To install Digital World Library, follow the steps according to your platform:

1. OS X and Linux:
   * Download libdw-2013-1.tar.gz from the URL given above
   * Open Terminal
   * Go the directory/folder where you save the file, e.g. if you save it to Mac's default Downloads folder, then type :
      cd $HOME/Downloads
   * Unzip the file, e.g. type :
      tar xzvf libdw-2013-1.tar.gz
   * Go to the libdw folder, e.g. type:
      cd libdw-2013-1
   * Install the library by typing:
      sudo python setup.py install

2. Windows:
   * Download libdw-2013-1.tar.gz from the URL given above
   * Unzip the file using 7-Zip (download from URL above)
   * Open CommandPrompt by typing "cmd" from the Start Menu
   * Go the directory/folder where you have unzipped the file, e.g. type :
      cd C:\Downloads\libdw-2013-1
   * Install the library by typing:
      python setup.py install

To install the USB to Serial driver, follow the steps on this website: http://www.ftdichip.com/Support/Documents/InstallGuides.htm
 

RUNNING SIMULATOR - SOAR
------------------------

After you have installed the Digital World Library, you can run the
simulator, called SOAR. To run it, follow the steps below:

1. OS X and Linux:
   * Open Terminal
   * Type : 
      soar &

2. Windows:
    * Open CommandPrompt by typing "cmd" from the Start Menu
    * Go to the folder where you store Digital World Library, e.g.:
       cd C:\Downloads\libdw-2013-1\
    * Go to "soar" folder:
       cd soar
    * Run soar by typing:
       python soar

USING SIMULATOR - SOAR
----------------------

1. Running the code in a simulated world:
   1.1. Run Soar as described above
   1.2. Click "Simulator" button and choose the Python files for the "Worlds"
   1.3. Click "Brain" button and choose the Python files containing your robot brain
   1.4. Click "Start" Button to start simulation
   1.5. Click "Stop" Button to stop simulation
   1.6. Click "Step" Button to run simulation in time steps

2. Running the code and connect to Amigobot using wired connection:
   2.1. Make sure you have installed USB to Serial driver according to your platform
   2.2. Connect the USB to your laptop and the Serial RS-232 to Amigobot
   2.3. Run Soar 
   2.4. Click "Simulator" button to load any Python files for the "Worlds"
   2.5. Click "Brain" button and choose the Python files containing your robot brain
   2.6. Click "Amigobot" button to start connection with Amigobot
   2.7. Click "Start" button to start your program on Amigobot

3. Running the code and connect to Amigobot using wireless connection:
   3.1. Make sure you have installed USB to Serial driver according to your platform
   3.2. Connect the USB to your laptop and the Serial RS-232 to WiBox
   3.3. Run Soar 
   3.4. Click "Simulator" button to load any Python files for the "Worlds"
   3.5. Click "Brain" button and choose the Python files containing your robot brain
   3.6. Click "Amigobot" button to start connection with Amigobot
   3.7. Click "Start" button to start your program on Amigobot

WORLD
-----
Some World files for simulation has been created ans it is part of the Digital Library Package. It is also included in this package under the folder "worlds".

BRAIN
-----
A simple Brain file has been included: smBrain.py.

DOCUMENTATION
-------------

* Details on 2D design: http://people.sutd.edu.sg/~aditya_mathur/

* Digital World Library:
http://mit.edu/6.01/www/documentation/index.html

* Amigobot: http://robots.mobilerobots.com/wiki/Main_Page 


Author: Oka Kurniawan
email: oka_kurniawan@sutd.edu.sg


