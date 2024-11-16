import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, pyqtSignal

class CircularProgressBar(QWidget):
    progress_finished = pyqtSignal()
    
    def __init__(self, duration, x, y, parent=None):
        super().__init__(parent)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.done = None
        
        layout = QVBoxLayout(self)
        
        layout.addWidget(self.progress_bar)
        
        self.duration = duration
        
        self.elasped_time = 0
        
        self.timer = QTimer(self)
        
        self.timer.timeout.connect(self.update_progress)
        
        self.move(x, y)
                                
    def update_progress(self):
        self.elasped_time += 1
        progress_value = int((self.elasped_time/ self.duration) * 100)
        
        self.progress_bar.setValue(progress_value)
        
        if progress_value >= 100:
            self.timer.stop()
            self.close()
            self.progress_finished.emit()
            
    def start_progress(self):
        self.show()
        self.elasped_time = 0
        self.progress_bar.setValue(0)
        self.timer.start(1000)
        
        
