import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication

from mainwindow import Ui_MainWindow

current_date = str(time.gmtime().tm_year) + "/" + str(time.gmtime().tm_mon) + "/" + str(time.gmtime().tm_mday)
current_time = str(time.gmtime().tm_hour) + ":" + str(time.gmtime().tm_min) + ":" + str(time.gmtime().tm_sec)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.date.setText("Current date is: " + current_date)    
        self.ui.time.setText("Time of execution is: " + current_time)   

        def exit_application(self):
            QCoreApplication.quit()

        self.ui.pushButton.clicked.connect(exit_application)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
