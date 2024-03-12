#importing components
from PySide6.QtWidgets import QApplication, QWidget
import sys

#creating the application and handling events
app = QApplication(sys.argv)

#event loop
window = QWidget()
window.show()

#start the event loop
app.exec()