import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QWidget

class ChessGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    ## Initializing the user interface
    def initUI(self, X = 100, Y = 100, W = 800, H = 800):
        self.setGeometry(X, Y, W, H)
        self.setWindowTitle('Chess Game')

        scene = QGraphicsScene(self)
        view = QGraphicsView(scene, self)
        self.setCentralWidget(view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chess = ChessGame()
    chess.show()
    sys.exit(app.exec())