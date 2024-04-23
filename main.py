import sys
import threading
import string
import time
from pynput.keyboard import Key, Listener
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from os import listdir
from os.path import isfile, join


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Input Display v0.1 beta")
        self.resize(800, 400)
        self.move(0, 700)
        
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


        # key animation
        # (only insert, print screen, home, page up, page down, end, are missing. delete is preserved to close listener)
        files = list()
        for f in listdir("assets/"):
            if isfile(join("assets/", f)):
                setattr(self, f[:-4], QPixmap(f'assets/{f}'))


        # esc
        self.esc_bg = QLabel(self)
        self.esc_bg.setPixmap(self.key_rect_fg.scaled(66, 33))
        self.esc_bg.move(0, 10)

        self.esc = QLabel(self)
        self.esc.setPixmap(self.key_esc.scaled(66, 33))
        self.esc.move(0, 10)

        # tab
        self.tab_bg = QLabel(self)
        self.tab_bg.setPixmap(self.key_rect_fg.scaled(100, 50))
        self.tab_bg.move(20, 60)

        self.tab = QLabel(self)
        self.tab.setPixmap(self.key_tab.scaled(100, 50))
        self.tab.move(20, 60)

        # shift
        self.lshift_bg = QLabel(self)
        self.lshift_bg.setPixmap(self.key_rect_fg.scaled(100, 50))
        self.lshift_bg.move(20, 120)

        self.lshift = QLabel(self)
        self.lshift.setPixmap(self.key_shift.scaled(100, 50))
        self.lshift.move(20, 120)


        # w
        self.w_bg = QLabel(self)
        self.w_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.w_bg.move(190, 60)

        self.w = QLabel(self)
        self.w.setPixmap(self.key_w.scaled(50, 50))
        self.w.move(190, 60)

        # a
        self.a_bg = QLabel(self)
        self.a_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.a_bg.move(160, 120)

        self.a = QLabel(self)
        self.a.setPixmap(self.key_a.scaled(50, 50))
        self.a.move(160, 120)

        # s
        self.s_bg = QLabel(self)
        self.s_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.s_bg.move(220, 120)

        self.s = QLabel(self)
        self.s.setPixmap(self.key_s.scaled(50, 50))
        self.s.move(220, 120)

        # d
        self.d_bg = QLabel(self)
        self.d_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.d_bg.move(280, 120)

        self.d = QLabel(self)
        self.d.setPixmap(self.key_d.scaled(50, 50))
        self.d.move(280, 120)


        # e
        self.e_bg = QLabel(self)
        self.e_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.e_bg.move(300, 60)

        self.e = QLabel(self)
        self.e.setPixmap(self.key_e.scaled(50, 50))
        self.e.move(300, 60)

        # r
        self.r_bg = QLabel(self)
        self.r_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.r_bg.move(360, 60)

        self.r = QLabel(self)
        self.r.setPixmap(self.key_r.scaled(50, 50))
        self.r.move(360, 60)


        # c
        self.c_bg = QLabel(self)
        self.c_bg.setPixmap(self.key_square_fg.scaled(50, 50))
        self.c_bg.move(130, 180)

        self.c = QLabel(self)
        self.c.setPixmap(self.key_c.scaled(50, 50))
        self.c.move(130, 180)

        # space
        self.space_bg = QLabel(self)
        self.space_bg.setPixmap(self.key_space_fg.scaled(150, 50))
        self.space_bg.move(200, 180)


        # enter
        self.enter_bg = QLabel(self)
        self.enter_bg.setPixmap(self.key_rect_fg.scaled(100, 50))
        self.enter_bg.move(370, 120)

        self.enter = QLabel(self)
        self.enter.setPixmap(self.key_enter.scaled(100, 50))
        self.enter.move(370, 120)


        self.show()


def on_press(key):
    print(key)
    if key == Key.delete:
        return False

    try:
        if key.char.lower() == 'w':
            window.w_bg.setPixmap(window.key_square_bg.scaled(50, 50))
        if key.char.lower() == 'a':
            window.a_bg.setPixmap(window.key_square_bg.scaled(50, 50))
        if key.char.lower() == 's':
            window.s_bg.setPixmap(window.key_square_bg.scaled(50, 50))
        if key.char.lower() == 'd':
            window.d_bg.setPixmap(window.key_square_bg.scaled(50, 50))

        if key.char.lower() == 'e':
            window.e_bg.setPixmap(window.key_square_bg.scaled(50, 50))
        if key.char.lower() == 'r':
            window.r_bg.setPixmap(window.key_square_bg.scaled(50, 50))
        if key.char.lower() == 'c':
            window.c_bg.setPixmap(window.key_square_bg.scaled(50, 50))
            
    except AttributeError:
        if key == Key.esc:
            window.esc_bg.setPixmap(window.key_rect_bg.scaled(66, 33))
        if key == Key.tab:
            window.tab_bg.setPixmap(window.key_rect_bg.scaled(100, 50))
        if key == Key.shift:
            window.lshift_bg.setPixmap(window.key_rect_bg.scaled(100, 50))
        if key == Key.enter:
            window.enter_bg.setPixmap(window.key_rect_bg.scaled(100, 50))
        if key == Key.space:
            window.space_bg.setPixmap(window.key_space_bg.scaled(150, 50))
        

def on_release(key):
    try:
        if key.char.lower() == 'w':
            window.w_bg.setPixmap(window.key_square_fg.scaled(50, 50))
        if key.char.lower() == 'a':
            window.a_bg.setPixmap(window.key_square_fg.scaled(50, 50))
        if key.char.lower() == 's':
            window.s_bg.setPixmap(window.key_square_fg.scaled(50, 50))
        if key.char.lower() == 'd':
            window.d_bg.setPixmap(window.key_square_fg.scaled(50, 50))

        if key.char.lower() == 'e':
            window.e_bg.setPixmap(window.key_square_fg.scaled(50, 50))
        if key.char.lower() == 'r':
            window.r_bg.setPixmap(window.key_square_fg.scaled(50, 50))
        if key.char.lower() == 'c':
            window.c_bg.setPixmap(window.key_square_fg.scaled(50, 50))

    except AttributeError:
        if key == Key.esc:
            window.esc_bg.setPixmap(window.key_rect_fg.scaled(66, 33))
        if key == Key.tab:
            window.tab_bg.setPixmap(window.key_rect_fg.scaled(100, 50))
        if key == Key.shift:
            window.lshift_bg.setPixmap(window.key_rect_fg.scaled(100, 50))
        if key == Key.enter:
            window.enter_bg.setPixmap(window.key_rect_fg.scaled(100, 50))
        if key == Key.space:
            window.space_bg.setPixmap(window.key_space_fg.scaled(150, 50))

def log():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


thread1 = threading.Thread(target=log)
thread1.start()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())




