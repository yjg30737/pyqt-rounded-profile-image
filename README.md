# pyqt-rounded-profile-image
PyQt rounded profile image like Youtube, Google, etc.

Profile image is `QLabel`. `QPixmap`'s `setMask` fucntion is being used to make the image rounded. 

## Requirements
* PyQt5

## Install
### clone
* git clone ~
* python sample.py
### as a package
* python -m pip install pyqt-rounded-profile-image

## Method Overview
* `setImage(filename: str)` - Set the image file to the circle.

## Example
### Code Sample
```python
import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog

from pyqt_rounded_profile_image import RoundedImage


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__label = RoundedImage()
        
        # maximum size has to be set
        # otherwise, it will expand, regardless of the size policy setting
        # half of the actual size is recommended
        self.__label.setMaximumSize(128, 128)

        btn = QPushButton('Select the Image')
        btn.clicked.connect(self.__update)

        lay = QVBoxLayout()
        lay.addWidget(self.__label)
        lay.addWidget(btn)
        lay.setAlignment(Qt.AlignCenter)
        self.setLayout(lay)
        
        # set the image file name you want (as an default image)
        self.__label.setImage('a.png')

    def __update(self):
        # os.path.expanduser indicates the "Document" folder
        filename = QFileDialog.getOpenFileName(self, 'Select the Image', os.path.expanduser('~'), 'Image Files (*.png *.jpg *.bmp)')
        if filename[0]:
            filename = filename[0]
            self.__label.setImage(filename)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
```

### Result

![image](https://user-images.githubusercontent.com/55078043/215319608-4c0e95dd-06f8-400d-8d51-ed516a49fe88.png)

You can select the image file to show (*.png, *.jpg, *.bmp)

There are two images (both two are Laurie Holden) in the root directory for testing the feature.

## TODO list
* Default image or text
* Popup window
* Animation
* Ensure that the edges are smoother, regardless of the size
