
from __future__ import print_function
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QMouseEvent, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMessageBox, QTextEdit, QFileDialog, QHBoxLayout, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import sys
import res
import os
import struct
import marshal
import zlib
import sys
import tempfile
from subprocess import run as sp
import requests
from uuid import uuid4 as uniquename

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectedFile = ""
        self._is_dragging = False
        self._start_drag_pos = QPoint()
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setFixedSize(243, 415)
        MainWindow.setStyleSheet(u"border-image:none;\n"
"color:white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainMenu = QFrame(self.centralwidget)
        self.MainMenu.setObjectName(u"MainMenu")
        self.MainMenu.setGeometry(QRect(3, 20, 238, 392))
        self.MainMenu.setAutoFillBackground(False)
        self.MainMenu.setStyleSheet(u"border-image:url(:background/back.jpeg);\n"
"border-radius:20px;")
        self.MainMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.ToolTitle = QLabel(self.MainMenu)
        self.ToolTitle.setObjectName(u"ToolTitle")
        self.ToolTitle.setGeometry(QRect(60, 10, 120, 50))
        font = QFont()
        font.setPointSize(18)
        self.ToolTitle.setFont(font)
        self.ToolTitle.setStyleSheet(u"border-image:none;")
        self.uploadFIleBut = QPushButton(self.MainMenu)
        self.uploadFIleBut.setObjectName(u"uploadFIleBut")
        self.uploadFIleBut.clicked.connect(self.fileget)
        self.uploadFIleBut.setGeometry(QRect(30, 180, 190, 24))
        self.uploadFIleBut.setStyleSheet(u"            QPushButton {\n"
"                color: black;\n"
"                background-color: #F5F5F5;\n"
"                border: 1px solid #375174;\n"
"                border-radius: 5px;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c4c4c4;\n"
"                border: 1px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #9c9c9c;\n"
"                border: 1px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:disabled {\n"
"                background-color: #aaaaaa;\n"
"                color: #666666;\n"
"                border-image:none;\n"
"            }")
        self.text1 = QLabel(self.MainMenu)
        self.text1.setObjectName(u"text1")
        self.text1.setGeometry(QRect(32, 159, 120, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.text1.setFont(font1)
        self.text1.setStyleSheet(u"color: #fff;\n"
"border-image:none;")
        self.author = QLabel(self.MainMenu)
        self.author.setObjectName(u"author")
        self.author.setGeometry(QRect(80, 370, 90, 16))
        self.author.setStyleSheet(u"border-image:none;")
        self.startBut = QPushButton(self.MainMenu)
        self.startBut.setObjectName(u"startBut")
        self.startBut.clicked.connect(self.startEngine)
        self.startBut.setGeometry(QRect(80, 220, 90, 20))
        self.startBut.setStyleSheet(u"            QPushButton {\n"
"                color: black;\n"
"                background-color: #F5F5F5;\n"
"                border: 1px solid #375174;\n"
"                border-radius: 5px;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c4c4c4;\n"
"                border: 1px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #9c9c9c;\n"
"                border: 1px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:disabled {\n"
"                background-color: #aaaaaa;\n"
"                color: #666666;\n"
"                border-image:none;\n"
"            }")
#         self.outputtext = QLabel(self.MainMenu)
#         self.outputtext.setObjectName(u"outputtext")
#         self.outputtext.setGeometry(QRect(10, 260, 81, 20))
#         self.outputtext.setFont(font1)
#         self.outputtext.setStyleSheet(u"color: #fff;\n"
# "border-image:none;")
#         self.outputbox = QTextEdit(self.MainMenu)
#         self.outputbox.setObjectName(u"outputbox")
#         self.outputbox.setGeometry(QRect(10, 280, 220, 90))
#         self.outputbox.setReadOnly(True)
#         self.outputbox.setStyleSheet(u"color:black;border-image: none;\n"
# "")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(20, 0, 200, 20))
        self.header.setStyleSheet(u"background-color:#2c2c2c;\n"
"border-radius:5px;")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.fileName = QLabel(self.MainMenu)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(50, 290, 150, 20))
        self.fileName.setFont(font1)
        self.fileName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fileName.setStyleSheet(u"color: #fff;\n"
"border-image:none;")
        self.horizontalLayoutWidget = QWidget(self.header)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 0, 124, 20))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeBut = QPushButton(self.horizontalLayoutWidget)
        self.minimizeBut.setObjectName(u"minimizeBut")
        self.minimizeBut.setStyleSheet(u"            QPushButton {\n"
"                color: white;\n"
"                background-color: none;\n"
"                border: 0px solid #375174;\n"
"                border-radius: 5px;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:hover {\n"
"				 color: gray;\n"
"                background-color: none;\n"
"                border: 0px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: none;\n"
"                border: 0px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:disabled {\n"
"                background-color: none;\n"
"                color: #666666;\n"
"                border-image:none;\n"
"            }")
        icon = QIcon()
        icon.addFile(u":/background/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBut.setIcon(icon)
        self.minimizeBut.setIconSize(QSize(20, 16))

        self.horizontalLayout.addWidget(self.minimizeBut)

        self.exitBut = QPushButton(self.horizontalLayoutWidget)
        self.exitBut.setObjectName(u"exitBut")
        self.exitBut.setStyleSheet(u"            QPushButton {\n"
"                color: white;\n"
"                background-color: none;\n"
"                border: 0px solid #375174;\n"
"                border-radius: 5px;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:hover {\n"
"				 color: gray;\n"
"                background-color: none;\n"
"                border: 0px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: none;\n"
"                border: 0px solid #F5F5F5;\n"
"                border-image:none;\n"
"            }\n"
"            QPushButton:disabled {\n"
"                background-color: none;\n"
"                color: #666666;\n"
"                border-image:none;\n"
"            }")
        icon1 = QIcon()
        icon1.addFile(u":/background/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exitBut.setIcon(icon1)
        self.exitBut.setIconSize(QSize(20, 16))

        self.horizontalLayout.addWidget(self.exitBut)

        MainWindow.setCentralWidget(self.centralwidget)
        self.exitBut.pressed.connect(MainWindow.close)
        self.minimizeBut.pressed.connect(MainWindow.showMinimized)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToolTitle.setText(QCoreApplication.translate("MainWindow", u"PyDec v0.1", None))
        self.uploadFIleBut.setText(QCoreApplication.translate("MainWindow", u"Upload file", None))
        self.text1.setText(QCoreApplication.translate("MainWindow", u"Support python only.", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"Author : xStrong", None))
        self.startBut.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.fileName.setText(QCoreApplication.translate("MainWindow", u"No file has been selected.", None))
        self.exitBut.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        # self.outputtext.setText(QCoreApplication.translate("MainWindow", u"output box", None))
        self.minimizeBut.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.header.geometry().contains(event.position().toPoint()):
            self._is_dragging = True
            self._start_drag_pos = event.globalPosition().toPoint() - self.pos()
            event.accept()
    def mouseMoveEvent(self, event: QMouseEvent):
        if self._is_dragging:
            self.move(event.globalPosition().toPoint() - self._start_drag_pos)
            event.accept()
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()
    def fileget(self):
        self.selectedFile, _ = QFileDialog.getOpenFileName(parent=self, caption="Select the exe python file.", filter="Executable (*.exe)")
        # os.rename(extracted, os.path.basename(extracted))
        # self.selectedFile = os.path.basename(extracted)
        self.fileName.setText(os.path.basename(self.selectedFile))
    def startEngine(self):
        # pass
        arch = PyInstArchive(self.selectedFile)
        if arch.open():
            if arch.checkFile():
                if arch.getCArchiveInfo():
                    arch.parseTOC()
                    arch.extractFiles( )
                    arch.close()
                    return
            arch.close()
class CTOCEntry:
    def __init__(self, position, cmprsdDataSize, uncmprsdDataSize, cmprsFlag, typeCmprsData, name):
        self.position = position
        self.cmprsdDataSize = cmprsdDataSize
        self.uncmprsdDataSize = uncmprsdDataSize
        self.cmprsFlag = cmprsFlag
        self.typeCmprsData = typeCmprsData
        self.name = name


class PyInstArchive(QObject):
    PYINST20_COOKIE_SIZE = 24           # For pyinstaller 2.0
    PYINST21_COOKIE_SIZE = 24 + 64      # For pyinstaller 2.1+
    MAGIC = b'MEI\014\013\012\013\016'  # Magic number which identifies pyinstaller
    
    def __init__(self, path):
        self.filePath = path
        self.pycMagic = b'\0' * 4
        self.barePycList = [] # List of pyc's whose headers have to be fixed
    def open(self):
        try:
            
            self.fPtr = open(self.filePath, 'rb')
            self.fileSize = os.stat(self.filePath).st_size
        except:
            # print('[!] Error: Could not open {0}'.format(self.filePath))
            return False
        return True


    def close(self):
        try:
            self.fPtr.close()
        except:
            pass


    def checkFile(self):
        # print('[+] Processing {0}'.format(self.filePath))

        searchChunkSize = 8192
        endPos = self.fileSize
        self.cookiePos = -1

        if endPos < len(self.MAGIC):
            self.msgBox("[!] Error : File is too short or truncated")
            return False

        while True:
            startPos = endPos - searchChunkSize if endPos >= searchChunkSize else 0
            chunkSize = endPos - startPos

            if chunkSize < len(self.MAGIC):
                break

            self.fPtr.seek(startPos, os.SEEK_SET)
            data = self.fPtr.read(chunkSize)

            offs = data.rfind(self.MAGIC)

            if offs != -1:
                self.cookiePos = startPos + offs
                break

            endPos = startPos + len(self.MAGIC) - 1

            if startPos == 0:
                break

        if self.cookiePos == -1:
            self.msgBox("[!] Error : Missing cookie, unsupported pyinstaller version or not a pyinstaller archive")
            return False

        self.fPtr.seek(self.cookiePos + self.PYINST20_COOKIE_SIZE, os.SEEK_SET)

        if b'python' in self.fPtr.read(64).lower():
            # print('[+] Pyinstaller version: 2.1+')
            self.pyinstVer = 21     # pyinstaller 2.1+
        else:
            self.pyinstVer = 20     # pyinstaller 2.0
            # print('[+] Pyinstaller version: 2.0')

        return True


    def getCArchiveInfo(self):
        try:
            if self.pyinstVer == 20:
                self.fPtr.seek(self.cookiePos, os.SEEK_SET)

                # Read CArchive cookie
                (magic, lengthofPackage, toc, tocLen, pyver) = \
                struct.unpack('!8siiii', self.fPtr.read(self.PYINST20_COOKIE_SIZE))

            elif self.pyinstVer == 21:
                self.fPtr.seek(self.cookiePos, os.SEEK_SET)

                # Read CArchive cookie
                (magic, lengthofPackage, toc, tocLen, pyver, pylibname) = \
                struct.unpack('!8sIIii64s', self.fPtr.read(self.PYINST21_COOKIE_SIZE))

        except:
            self.msgBox("[!] Error : The file is not a pyinstaller archive")
            return False

        self.pymaj, self.pymin = (pyver//100, pyver%100) if pyver >= 100 else (pyver//10, pyver%10)
        # print('[+] Python version: {0}.{1}'.format(self.pymaj, self.pymin))

        # Additional data after the cookie
        tailBytes = self.fileSize - self.cookiePos - (self.PYINST20_COOKIE_SIZE if self.pyinstVer == 20 else self.PYINST21_COOKIE_SIZE)

        # Overlay is the data appended at the end of the PE
        self.overlaySize = lengthofPackage + tailBytes
        self.overlayPos = self.fileSize - self.overlaySize
        self.tableOfContentsPos = self.overlayPos + toc
        self.tableOfContentsSize = tocLen

        # print('[+] Length of package: {0} bytes'.format(lengthofPackage))
        return True


    def parseTOC(self):
        # Go to the table of contents
        self.fPtr.seek(self.tableOfContentsPos, os.SEEK_SET)

        self.tocList = []
        parsedLen = 0

        # Parse table of contents
        while parsedLen < self.tableOfContentsSize:
            (entrySize, ) = struct.unpack('!i', self.fPtr.read(4))
            nameLen = struct.calcsize('!iIIIBc')

            (entryPos, cmprsdDataSize, uncmprsdDataSize, cmprsFlag, typeCmprsData, name) = \
            struct.unpack( \
                '!IIIBc{0}s'.format(entrySize - nameLen), \
                self.fPtr.read(entrySize - 4))

            try:
                name = name.decode("utf-8").rstrip("\0")
            except UnicodeDecodeError:
                newName = str(uniquename())
                # print('[!] Warning: File name {0} contains invalid bytes. Using random name {1}'.format(name, newName))
                name = newName
            
            # Prevent writing outside the extraction directory
            if name.startswith("/"):
                name = name.lstrip("/")

            if len(name) == 0:
                name = str(uniquename())
                # print('[!] Warning: Found an unamed file in CArchive. Using random name {0}'.format(name))

            self.tocList.append( \
                                CTOCEntry(                      \
                                    self.overlayPos + entryPos, \
                                    cmprsdDataSize,             \
                                    uncmprsdDataSize,           \
                                    cmprsFlag,                  \
                                    typeCmprsData,              \
                                    name                        \
                                ))

            parsedLen += entrySize
        # print('[+] Found {0} files in CArchive'.format(len(self.tocList)))


    def _writeRawData(self, filepath, data):
        nm = filepath.replace('\\', os.path.sep).replace('/', os.path.sep).replace('..', '__')
        nmDir = os.path.dirname(nm)
        if nmDir != '' and not os.path.exists(nmDir): # Check if path exists, create if not
            os.makedirs(nmDir)

        with open(nm, 'wb') as f:
            f.write(data)


    def extractFiles(self):
        # print('[+] Beginning extraction...please standby')

        currentPath = os.getcwd()
        tempdir = tempfile.TemporaryDirectory()
        os.chdir(tempdir.name)

        for entry in self.tocList:
            self.fPtr.seek(entry.position, os.SEEK_SET)
            data = self.fPtr.read(entry.cmprsdDataSize)

            if entry.cmprsFlag == 1:
                try:
                    data = zlib.decompress(data)
                except zlib.error:
                    # print('[!] Error : Failed to decompress {0}'.format(entry.name))
                    continue
                # Malware may tamper with the uncompressed size
                # Comment out the assertion in such a case
                assert len(data) == entry.uncmprsdDataSize # Sanity Check

            if entry.typeCmprsData == b'd' or entry.typeCmprsData == b'o':
                # d -> ARCHIVE_ITEM_DEPENDENCY
                # o -> ARCHIVE_ITEM_RUNTIME_OPTION
                # These are runtime options, not files
                continue

            basePath = os.path.dirname(entry.name)
            if basePath != '':
                # Check if path exists, create if not
                if not os.path.exists(basePath):
                    os.makedirs(basePath)

            if entry.typeCmprsData == b's':
                # s -> ARCHIVE_ITEM_PYSOURCE
                # Entry point are expected to be python scripts
                # print('[+] Possible entry point: {0}.pyc'.format(entry.name))

                if self.pycMagic == b'\0' * 4:
                    # if we don't have the pyc header yet, fix them in a later pass
                    self.barePycList.append(entry.name + '.pyc')
                self._writePyc(entry.name + '.pyc', data)

            elif entry.typeCmprsData == b'M' or entry.typeCmprsData == b'm':
                # M -> ARCHIVE_ITEM_PYPACKAGE
                # m -> ARCHIVE_ITEM_PYMODULE
                # packages and modules are pyc files with their header intact

                # From PyInstaller 5.3 and above pyc headers are no longer stored
                # https://github.com/pyinstaller/pyinstaller/commit/a97fdf
                if data[2:4] == b'\r\n':
                    # < pyinstaller 5.3
                    if self.pycMagic == b'\0' * 4: 
                        self.pycMagic = data[0:4]
                    self._writeRawData(entry.name + '.pyc', data)

                else:
                    # >= pyinstaller 5.3
                    if self.pycMagic == b'\0' * 4:
                        # if we don't have the pyc header yet, fix them in a later pass
                        self.barePycList.append(entry.name + '.pyc')

                    self._writePyc(entry.name + '.pyc', data)

            else:
                self._writeRawData(entry.name, data)

                if entry.typeCmprsData == b'z' or entry.typeCmprsData == b'Z':
                    self._extractPyz(entry.name)

        # Fix bare pyc's if any
        self._fixBarePycs()

        # for item in os.listdir():
        #     if item ==  os.path.basename(str(self.filePath)).replace('.exe', '.pyc'):
        #         continue
        #     if os.path.isdir(item):
        #         shutil.rmtree(item)
        #     elif os.path.isfile(item):
        #         os.remove(item)

        def pycDec():
            pathFile = os.getcwd()
            # Check the file if exists or not!
            try:
                api = "https://api.pylingual.io/upload"
                fileName = os.path.basename(str(self.filePath)).replace('.exe', '')
                fullFilePath = os.path.join(pathFile, fileName+".pyc")
                with open(fullFilePath, "rb") as f:
                    file_raw = f.read()
                fileData = {"file": (file_raw), "fileName": f"{fileName}.pyc"}
                res = requests.post(api, files=fileData)
                if res.ok:
                    identifier = res.json()["identifier"]
                    getPyFile(identifier, fileName)
            except:
                self.msgBox("PyDec doesn't support this file.")
                return False
        def getPyFile(url_identifier, fileName):
            s1 = requests.Session()
            decoded_python = "https://api.pylingual.io/view_chimera?identifier={}".format(url_identifier)
            res = s1.get(decoded_python)
            if res.ok:
                file_source = res.json()["editor_content"]["file_raw_python"]["editor_content"]
                file_source = str(file_source).replace("# Decompiled with PyLingual (https://pylingual.io)", "")
                os.chdir(currentPath)
                tempdir.cleanup()
                with open(fileName+".py", mode="w+", encoding="UTF-8") as f:
                    f.write(str(file_source))
                    f.close()
                os.startfile(os.path.dirname(os.path.abspath(__file__)))
        
        pycDec()
    
    def msgBox(self, msg):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Icon.Information)
        msgbox.setWindowTitle("Report")
        msgbox.setText(msg)
        msgbox.setStyleSheet("background:black;color:white;")
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgbox.exec()

    def _fixBarePycs(self):
        for pycFile in self.barePycList:
            with open(pycFile, 'r+b') as pycFile:
                # Overwrite the first four bytes
                pycFile.write(self.pycMagic)


    def _writePyc(self, filename, data):
        with open(filename, 'wb') as pycFile:
            pycFile.write(self.pycMagic)            # pyc magic

            if self.pymaj >= 3 and self.pymin >= 7:                # PEP 552 -- Deterministic pycs
                pycFile.write(b'\0' * 4)        # Bitfield
                pycFile.write(b'\0' * 8)        # (Timestamp + size) || hash 

            else:
                pycFile.write(b'\0' * 4)      # Timestamp
                if self.pymaj >= 3 and self.pymin >= 3:
                    pycFile.write(b'\0' * 4)  # Size parameter added in Python 3.3

            pycFile.write(data)


    def _extractPyz(self, name):
        
        dirName =  name
        # Create a directory for the contents of the pyz
        if not os.path.exists(dirName):
            os.mkdir(dirName)

        with open(name, 'rb') as f:
            pyzMagic = f.read(4)
            assert pyzMagic == b'PYZ\0' # Sanity Check

            pyzPycMagic = f.read(4) # Python magic value

            if self.pycMagic == b'\0' * 4:
                self.pycMagic = pyzPycMagic

            elif self.pycMagic != pyzPycMagic:
                self.pycMagic = pyzPycMagic
                # print('[!] Warning: pyc magic of files inside PYZ archive are different from those in CArchive')

            # Skip PYZ extraction if not running under the same python version
            if self.pymaj != sys.version_info.major or self.pymin != sys.version_info.minor:
                # print('[!] Warning: This script is running in a different Python version than the one used to build the executable.')
                # print('[!] Please run this script in Python {0}.{1} to prevent extraction errors during unmarshalling'.format(self.pymaj, self.pymin))
                # print('[!] Skipping pyz extraction')
                return

            (tocPosition, ) = struct.unpack('!i', f.read(4))
            f.seek(tocPosition, os.SEEK_SET)

            try:
                toc = marshal.load(f)
            except:
                print('[!] Unmarshalling FAILED. Cannot extract {0}. Extracting remaining files.'.format(name))
                return

            # print('[+] Found {0} files in PYZ archive'.format(len(toc)))

            # From pyinstaller 3.1+ toc is a list of tuples
            if type(toc) == list:
                toc = dict(toc)

            for key in toc.keys():
                global fileName
                (ispkg, pos, length) = toc[key]
                f.seek(pos, os.SEEK_SET)
                fileName = key

                try:
                    # for Python > 3.3 some keys are bytes object some are str object
                    fileName = fileName.decode('utf-8')
                except:
                    pass

                # Prevent writing outside dirName
                
                fileName = fileName.replace('..', '__').replace('.', os.path.sep)
                if ispkg == 1:
                    filePath = os.path.join(dirName, fileName, '__init__.pyc')

                else:
                    filePath = os.path.join(dirName, fileName + '.pyc')

                fileDir = os.path.dirname(filePath)
                if not os.path.exists(fileDir):
                    os.makedirs(fileDir)

                try:
                    data = f.read(length)
                    data = zlib.decompress(data)
                except:
                    print('[!] Error: Failed to decompress {0}, probably encrypted. Extracting as is.'.format(filePath))
                    open(filePath + '.encrypted', 'wb').write(data)
                else:
                    self._writePyc(filePath, data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
