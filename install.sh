echo "This script has to be run after ubuntut installation in order to install essential apps"
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install vlc
sudo apt-get install git
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
sudo apt-get install python-pygame
sudo apt-get -y install python2.7 python-pip python-dev
sudo apt-get -y install ipython ipython-notebook
sudo pip install --upgrade pip
sudo -H pip install jupyter
sudo pip install sklearn
sudo pip install xgboost
sudo pip install tensorflow
sudo apt-get install python-matplotlib
sudo pip install BeautifulSoup
sudo pip install seaborn
sudo apt-get install python-urllib3
sudo apt-get update && sudo apt-get install octave
sudo pip install lightgbm
sudo apt-get install libopencv-dev python-opencv
sudo pip install tqdm
sudo pip install futures
sudo pip install keras
#Installing Google Chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update 
sudo apt-get install google-chrome-stable




# echo "Installing dependancies for "
# sudo apt-get install -y build-essential cmake pkg-config
# sudo apt-get install -y libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
# sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
# sudo apt-get install -y libgtk2.0-dev
# sudo apt-get install -y libatlas-base-dev gfortran
# sudo apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev

# curl -O https://bootstrap.pypa.io/get-pip.py
# sudo python3 get-pip.py
# sudo apt-get install -y python3.4-dev
# sudo pip install numpy

# echo "download OpenCV"

# cd ~
# git clone https://github.com/Itseez/opencv.git
# cd opencv
# git checkout 3.1.0
# cd ~
# git clone https://github.com/Itseez/opencv_contrib.git
# cd opencv_contrib
# git checkout 3.1.0

# echo "Compiling OpenCV"

# cd ~/opencv
# mkdir build
# cd build
# cmake -D CMAKE_BUILD_TYPE=RELEASE \
#       -D CMAKE_INSTALL_PREFIX=/usr/local \
#       -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
#       -D BUILD_opencv_python3=ON \
#       -D BUILD_EXAMPLES=ON ..
# sudo make -j4
# sudo make install
# sudo ldconfig



#Jayabhhs