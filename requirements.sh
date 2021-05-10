#!/bin/bash

# Get packages required for OpenCV

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools libatlas-base-dev


sudo apt-get install cmake

# Dlib for facial recognition
git clone https://github.com/davisking/dlib.git
cd dlib
sudo python3 setup.py install

cd

pip3 install face_recognition


# Need to get an older version of OpenCV because version 4 has errors
pip3 install opencv-python==3.4.6.27
pip3 install APScheduler==3.6.3
pip3 install certifi
pip3 install Pillow
pip3 install numpy 
pip3 install python-telegram-bot
pip3 install pytz
pip3 install schedule
pip3 install setuptools
pip3 install six
pip3 install pandas
pip3 install tornado
pip3 install tzlocal
pip3 install watchdog
pip3 install questionary


# Get packages required for TensorFlow
# Using the tflite_runtime packages available at https://www.tensorflow.org/lite/guide/python
# Will change to just 'pip3 install tensorflow' once newer versions of TF are added to piwheels

#pip3 install tensorflow

version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

if [ $version == "3.7" ]; then
pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
fi

if [ $version == "3.5" ]; then
pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp35-cp35m-linux_armv7l.whl
fi





