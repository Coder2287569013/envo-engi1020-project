from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import pygame
from pygame.math import Vector2
import sys
from time import monotonic
import random

pygame.init()

class GraphGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        pen = pg.mkPen(color=(255,0,0))
        pen2 = pg.mkPen(color=(0,255,0))
        pen3 = pg.mkPen(color=(0,0,255))

        self.plot_graph1 = pg.PlotWidget()
        self.plot_graph1.setBackground("#000000")
        self.plot_graph1.setLabel("left", "Temp")
        self.plot_graph1.setLabel("bottom", "Time")

        self.plot_graph2 = pg.PlotWidget()
        self.plot_graph2.setBackground("#000000")
        self.plot_graph2.setLabel("left", "Light")
        self.plot_graph2.setLabel("bottom", "Time")

        self.plot_graph3 = pg.PlotWidget()
        self.plot_graph3.setBackground("#000000")
        self.plot_graph3.setLabel("left", "Humidity")
        self.plot_graph3.setLabel("bottom", "Time")

        layout.addWidget(self.plot_graph1)
        layout.addWidget(self.plot_graph2)
        layout.addWidget(self.plot_graph3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.interval = 500

        self.x = []
        self.y = []
        self.points = []

        self.data = self.plot_graph1.plot(self.x, self.y, pen=pen)
        self.data2 = self.plot_graph2.plot(self.x, self.y, pen=pen2)
        self.data3 = self.plot_graph3.plot(self.x, self.y, pen=pen3)

        self.timer = QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        if len(self.x) > 10:
            self.x = self.x[1:]
            self.y = self.y[1:]
        point = Vector2(monotonic(), random.uniform(20.0, 28.0))
        self.points.append(point)
        self.x.append(point.x)
        self.y.append(point.y)

        self.data.setData(self.x, self.y)
        self.data2.setData(self.x, self.y)
        self.data3.setData(self.x, self.y)




app = QApplication(sys.argv)
main = GraphGUI()
main.show()
app.exec()


