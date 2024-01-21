import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor, QResizeEvent
from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image

class Rook(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_Rook.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

class Knight(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_Knight.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))
    
    def VerifyMove(self):
        pass

class Bishop(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_Bishop.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

    def VerifyMove(self):
        pass

class Queen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_Queen.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

    def VerifyMove(self):
        pass

class King(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_King.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

    def VerifyMove(self):
        pass

class White_King(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("Black_King.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))
    
    def invert_colors(image_path, output_path):
        original_image = Image.open("Black_King.png")
        invert_image = Image.eval("Black_King", lambda x: 255 - x)
        invert_image.save("") ## Ended off here

class Pawn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("BlackPawn.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))
    
    def VerifyMove(self):

        pass
    

    def Promote(self):
        pass

class White_Pawn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QPixmap("BlackPawn.png")
        self.setMinimumSize(32, 32)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        size = min(self.width(), self.height())
        qp.drawPixmap(0, 0, self.image.scaled(size, size, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

class Board(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.background = QtGui.QPixmap('chessboard2.jpg')

        for i in range(8):
            layout.setRowStretch(i, 1)
            layout.setColumnStretch(i, 1)

        for col in range(8):
            layout.addWidget(Pawn(), 1, col)

        Pieces = [ Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook() ]

        for row in range(1):
            for col, piece in enumerate(Pieces):
                layout.addWidget(piece, row, col)

        # This is the bottom section of the board (White)
        for col in range(8):
            layout.addWidget(White_Pawn(), 6, col)

        Second_Set = [White_Rook(), White_Knight(), White_Bishop(), White_Queen(), White_King(), White_Bishop(), White_Knight(), White_Rook()]

        #Right below this comment is suppose to be the rest of the pieces underneath where the white pawns lay
        for row in range(1):
            for col, piece in enumerate(Second_Set):
                layout.addWidget(piece, row, col)


    def minimumSize(self):
        return QtCore.QSize(769, 768)
    
    def sizesHint(self):
        return QtCore.QSize(768, 768)
    
    def resizeEvent(self, event):
        size = min(self.width(), self.height())
        rect = QtCore.QRect(0, 0, size, size)
        rect.moveCenter(self.rect().center())
        self.layout().setGeometry(rect)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        rect = self.layout().geometry()
        qp.drawPixmap(rect, self.background.scaled(rect.size(), aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio, transformMode=QtCore.Qt.TransformationMode.SmoothTransformation))

class ChessGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Template")

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QHBoxLayout(central)
        self.board = Board()
        layout.addWidget(self.board)
        self.table = QtWidgets.QTableWidget(1, 3)
        layout.addWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
board = Board()
board.show()
sys.exit(app.exec())