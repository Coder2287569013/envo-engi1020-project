from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

app = QApplication([])

for family in sorted(QFontDatabase.families()):
    print(family)