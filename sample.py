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
        self.__label.setMaximumSize(128, 128)

        btn = QPushButton('Select the Image')
        btn.clicked.connect(self.__update)

        lay = QVBoxLayout()
        lay.addWidget(self.__label)
        lay.addWidget(btn)
        lay.setAlignment(Qt.AlignCenter)
        self.setLayout(lay)

        self.__label.setImage('a.png')

    def __update(self):
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