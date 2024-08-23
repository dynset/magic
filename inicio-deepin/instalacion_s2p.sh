sudo -E apt install python3
sudo -E apt install python3-pil
sudo -E apt install python3-pyqt5
sudo -E apt install python3-opencv
sudo -E apt install python3-xlrd


#gphoto2
sudo -E apt install swig
sudo -E apt install git
sudo -E apt install libgphoto2-6
sudo -E apt install python3-dev
sudo -E apt install libgphoto2-dev
sudo -E apt install gphoto2
git clone https://github.com/jim-easterbrook/python-gphoto2.git
cd python-gphoto2
python3 setup.py build_swig
python3 setup.py build
sudo python3 setup.py install
sleep 1
cd ..
sudo rm -R python-gphoto2

#pyqt5-dev-tools
#qttools5-dev-tools

