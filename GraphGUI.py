from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import pygame
from pygame.math import Vector2
import sys
from time import monotonic
import random
from SensorRead import SensorRead

pygame.init()

class GraphGUI(QMainWindow):
    time = []
    temp = []
    humid = []
    light = []
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
        self.plot_graph2.setLabel("left", "Humidity")
        self.plot_graph2.setLabel("bottom", "Time")

        self.plot_graph3 = pg.PlotWidget()
        self.plot_graph3.setBackground("#000000")
        self.plot_graph3.setLabel("left", "Light")
        self.plot_graph3.setLabel("bottom", "Time")

        layout.addWidget(self.plot_graph1)
        layout.addWidget(self.plot_graph2)
        layout.addWidget(self.plot_graph3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.interval = 100

        self.data = self.plot_graph1.plot(self.time, self.temp, pen=pen)
        self.data2 = self.plot_graph2.plot(self.time, self.humid, pen=pen2)
        self.data3 = self.plot_graph3.plot(self.time, self.light, pen=pen3)

        self.timer = QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        if len(self.time) > 10:
            self.time = self.time[1:]
            self.temp = self.temp[1:]
            self.humid = self.humid[1:]
            self.light = self.light[1:]

        sensor_data = SensorRead().read_values()

        self.time.append(monotonic())
        self.temp.append(sensor_data["temperature"])
        self.humid.append(sensor_data["humidity"])
        self.light.append(sensor_data["light"])

        self.data.setData(self.time, self.temp)
        self.data2.setData(self.time, self.humid)
        self.data3.setData(self.time, self.light)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GraphGUI()
    main.show()
    app.exec()


