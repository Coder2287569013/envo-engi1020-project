from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
import sys
from time import monotonic
from SensorRead import SensorRead

class GraphGUI(QMainWindow):
    time = []
    temp = []
    humid = []
    light = []
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
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

        self.distance = QLabel("0 cm")

        layout.addWidget(self.plot_graph1)
        layout.addWidget(self.plot_graph2)
        layout.addWidget(self.plot_graph3)
        main_layout.addLayout(layout)

        main_layout.addWidget(self.distance)

        widget = QWidget()
        widget.setLayout(main_layout)
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
            self.time.pop(0)
            self.temp.pop(0)
            self.humid.pop(0)
            self.light.pop(0)

        sensor_data = SensorRead().read_values()

        self.time.append(monotonic())
        self.temp.append(sensor_data["temperature"])
        self.humid.append(sensor_data["humidity"])
        self.light.append(sensor_data["light"])

        if sensor_data["distance"] < 15:
            self.distance.setStyleSheet(
            "color: white; font-size: 20px; font-family: Century Gothic;"
            "font-weight: bold; border-radius: 10px; background-color: #DB0447; opacity: 0.3;")

        elif sensor_data["distance"] < 30:
            self.distance.setStyleSheet(
            "color: white; font-size: 20px; font-family: Century Gothic;"
            "font-weight: bold; border-radius: 10px; background-color: #E03602; opacity: 0.3;")

        else: 
            self.distance.setStyleSheet(
            "color: white; font-size: 20px; font-family: Century Gothic;"
            "font-weight: bold; border-radius: 10px; background-color: #027736; opacity: 0.3;")

        self.distance.setText(f"{sensor_data["distance"]} cm")
        self.distance.setAlignment(Qt.AlignCenter)

        self.data.setData(self.time, self.temp)
        self.data2.setData(self.time, self.humid)
        self.data3.setData(self.time, self.light)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GraphGUI()
    main.show()
    app.exec()


